from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LanguageSerializer, WordSerializer, LinkSerializer
from .models import Language, Word, Link
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from rest_framework import status
from django.core.exceptions import ValidationError, ObjectDoesNotExist


class LanguageViewSet(viewsets.ViewSet):
    queryset = Language.objects.all()
    lookup_field = 'symbol'


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
        serialzier = WordSerializer(self.queryset.filter(language__symbol=lang, word=word).select_related('language'),
                                    many=True)
        return Response(serialzier.data)

    @extend_schema(responses=WordSerializer)
    @action(['GET'], False, url_path=r'listlang/(?P<lang>\w+)')
    def list_by_lang(self, request, lang):
        serialzier = WordSerializer(self.queryset.filter(language__symbol=lang).select_related('language'), many=True)
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

    @extend_schema(responses=LinkSerializer)
    def list(self, request):
        serializer = LinkSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @extend_schema(responses=LinkSerializer, request=LinkSerializer)
    def create(self, request):
        serializer = LinkSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
