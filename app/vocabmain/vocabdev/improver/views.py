from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LanguageSerializer, WordSerializer, LinkSerializer
from .models import Language, Word, Link
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class LanguageViewSet(viewsets.ViewSet):

    queryset = Language.objects.all()
    lookup_field = 'symbol'


class WordViewSet(viewsets.ViewSet):

    queryset = Word.objects.all()

    def list(self, request):
        serialzier = WordSerializer(self.queryset, many=True)
        return Response(serialzier.data)


class LinkViewSet(viewsets.ViewSet):

    queryset = Link.objects.all()


def test_endpoint(request):
    message = 'test'
    return JsonResponse(message, safe=False)
    # return JsonResponse({'message': 'test'})


# @api_view(['GET'])
# def test_endpoint(request):
#     return Response({'message': 'test'})
