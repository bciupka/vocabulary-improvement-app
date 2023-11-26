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
from django.core.exceptions import ValidationError


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
        seriailzier = WordSerializer(data=request.data)
        if seriailzier.is_valid():
            try:
                seriailzier.save()
                return Response(seriailzier.data, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response(dict(e), status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(seriailzier.errors, status=status.HTTP_400_BAD_REQUEST)


class LinkViewSet(viewsets.ViewSet):
    queryset = Link.objects.all()


def test_endpoint(request):
    message = 'test'
    return JsonResponse(message, safe=False)
    # return JsonResponse({'message': 'test'})

# @api_view(['GET'])
# def test_endpoint(request):
#     return Response({'message': 'test'})
