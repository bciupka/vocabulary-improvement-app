from .models import Language, Word, Link
from rest_framework import serializers


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    language = serializers.CharField(source='language.language_eng')

    class Meta:
        model = Word
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')
    base = WordSerializer()
    translation = WordSerializer()

    class Meta:
        model = Link
        fields = '__all__'
