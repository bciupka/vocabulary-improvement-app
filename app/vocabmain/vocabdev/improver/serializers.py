from .models import VocabUser, Polish
from rest_framework import serializers


class VocabUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = VocabUser
        fields = ['name']


class PolishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polish
        fields = ['word']
