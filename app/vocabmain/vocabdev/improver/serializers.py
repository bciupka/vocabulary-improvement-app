from .models import Language, Word, Link
from rest_framework import serializers


class WordSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(queryset=Language.objects.all(), slug_field='symbol')

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


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
