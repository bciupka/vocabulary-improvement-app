from .models import Language, Word, Link
from rest_framework import serializers
from django.core.exceptions import ValidationError


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(queryset=Language.objects.all(), slug_field='symbol')

    def validate(self, attrs):
        if not attrs['word'].islower():
            raise ValidationError({'word': 'Only lowercase for word'})
        elif len(attrs) > 2:
            raise ValidationError({'lenght': 'Only 2 fields required'})
        return attrs

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
