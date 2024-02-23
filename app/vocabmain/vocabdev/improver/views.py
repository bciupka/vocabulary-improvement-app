from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LanguageSerializer, WordSerializer, LinkSerializer, PaginationGetLinkSerializer
from .models import Language, Word, Link
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from rest_framework import status
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from drf_spectacular.utils import OpenApiParameter
from django.db.models.functions import Random


class LinkPagination(PageNumberPagination):
    page_size = 3
    max_page_size = 50


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'symbol__iexact'


class WordViewSet(viewsets.ViewSet):
    queryset = Word.objects.all()
    permission_classes = (IsAuthenticated,)

    @extend_schema(responses=WordSerializer)
    def list(self, request):
        serialzier = WordSerializer(self.queryset, many=True)
        return Response(serialzier.data)

    @extend_schema(responses=WordSerializer)
    @action(['GET'], False, url_path=r'getlang/(?P<lang>\w+)/(?P<word>\w+)')
    def get_by_lang(self, request, lang, word):
        serialzier = WordSerializer(self.queryset.filter(language__symbol__iexact=lang,
                                                         word__iexact=word).select_related('language'), many=True)
        return Response(serialzier.data)

    @extend_schema(responses=WordSerializer)
    @action(['GET'], False, url_path=r'listlang/(?P<lang>\w+)')
    def list_by_lang(self, request, lang):
        serialzier = WordSerializer(self.queryset.filter(language__symbol__iexact=lang).select_related('language'),
                                    many=True)
        return Response(serialzier.data)

    @extend_schema(responses=WordSerializer, request=WordSerializer)
    def create(self, request):
        serializier = WordSerializer(data=request.data)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializier.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkViewSet(viewsets.ViewSet):
    queryset = Link.objects.all()
    permission_classes = (IsAuthenticated,)
    pagination_class = LinkPagination
    paginator = pagination_class()


    @extend_schema(responses=PaginationGetLinkSerializer, parameters=[
        OpenApiParameter(name='amount', required=False, type=int),
        OpenApiParameter(name='lang1', required=True, type=str),
        OpenApiParameter(name='lang2', required=True, type=str)])
    def list(self, request):
        amount = int(request.query_params.get('amount', 100))
        lang1 = request.query_params.get('lang1')
        lang2 = request.query_params.get('lang2')
        if not request.query_params.get('page'):
            self.queryset.filter(user=request.user).update(random_nr=Random())
        random_queryset = self.queryset.filter(user=request.user, base__language__symbol=lang1,
                                               translation__language__symbol=lang2).order_by('random_nr')[:amount]
        serializer = PaginationGetLinkSerializer(random_queryset, many=True)
        page = self.paginator.paginate_queryset(queryset=serializer.data, request=request)
        if page:
            return self.paginator.get_paginated_response(page)
        return Response(serializer.data)

    @extend_schema(responses=PaginationGetLinkSerializer, parameters=[
        OpenApiParameter(name='amount', required=False, type=int),
        OpenApiParameter(name='lang1', required=True, type=str),
        OpenApiParameter(name='lang2', required=True, type=str)])
    @action(['GET',], detail=False, url_path="random_list")
    def single_random_list(self, request):
        amount = int(request.query_params.get('amount', 100))
        lang1 = request.query_params.get('lang1')
        lang2 = request.query_params.get('lang2')
        serializer = PaginationGetLinkSerializer(
            self.queryset.filter(base__language__symbol=lang1, translation__language__symbol=lang2)
            .order_by('?')[:amount], many=True)
        return Response(serializer.data)

    @extend_schema(responses=LinkSerializer, request=LinkSerializer)
    def create(self, request):
        serializer = LinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
