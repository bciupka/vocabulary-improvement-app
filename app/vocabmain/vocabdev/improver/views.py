from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LanguageSerializer, WordSerializer, LinkSerializer
from .models import Language, Word, Link
from rest_framework.decorators import api_view
from django.http import JsonResponse


class LanguageViewSet(viewsets.ModelViewSet):

    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    lookup_field = 'symbol'


class WordViewSet(viewsets.ModelViewSet):

    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'word'


class LinkViewSet(viewsets.ModelViewSet):

    queryset = Link.objects.all()
    serializer_class = LinkSerializer


def test_endpoint(request):
    message = 'test'
    return JsonResponse(message, safe=False)
    # return JsonResponse({'message': 'test'})


# @api_view(['GET'])
# def test_endpoint(request):
#     return Response({'message': 'test'})
