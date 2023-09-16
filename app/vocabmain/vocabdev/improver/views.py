from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VocabUserSerializer, PolishSerializer
from .models import VocabUser, Polish


class VocabUserViewset(viewsets.ViewSet):

    queryset = VocabUser.objects.all()

    def list(self, request):
        serializer = VocabUserSerializer(self.queryset, many=True)

        return Response(serializer.data)


class PolishViewset(viewsets.ViewSet):

    queryset = Polish.objects.all()

    def list(self, request):
        serializer = PolishSerializer(self.queryset, many=True)

        return Response(serializer.data)
