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
        if Word.objects.filter(language=attrs['language'], word=attrs['word'].lower()).exists():
            raise ValidationError({'word': 'Duplicate for language'})
        return attrs

    def create(self, validated_data):
        if not validated_data['word'].islower():
            validated_data['word'] = validated_data['word'].lower()
        return super().create(validated_data)

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
