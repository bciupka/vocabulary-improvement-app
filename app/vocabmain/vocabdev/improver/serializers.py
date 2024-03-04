from .models import Language, Word, Link
from rest_framework import serializers
from django.core.exceptions import ValidationError
from drf_spectacular.utils import extend_schema_field

class WordSerializer(serializers.ModelSerializer):
    language = serializers.SlugRelatedField(queryset=Language.objects.all(), slug_field='symbol')

    class Meta:
        model = Word
        fields = '__all__'
        validators = [serializers.UniqueTogetherValidator(queryset=Word.objects.all(), fields=['word', 'language'])]

    def to_internal_value(self, data):
        data['word'] = data['word'].lower()
        return super().to_internal_value(data)


class WordForLinkSerializer(WordSerializer):
    def __init__(self):
        super().__init__()
        self.Meta.validators = []


class LinkSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    base = WordForLinkSerializer()
    translation = WordForLinkSerializer()

    class Meta:
        model = Link
        exclude = ('random_nr',)

    def validate(self, attrs):
        if Link.objects.filter(user=attrs['user'],
                               base__word=attrs['base']['word'], base__language=attrs['base']['language'],
                               translation__word=attrs['translation']['word'],
                               translation__language=attrs['translation']['language']).exists():
            raise ValidationError({'link': 'Duplicated link'})
        if attrs['base']['language'] == attrs['translation']['language']:
            raise ValidationError({'link': 'Translation in same language is forbidden'})
        return super().validate(attrs)

    def create(self, validated_data):
        base, _ = Word.objects.get_or_create(**validated_data['base'])
        translation, _ = Word.objects.get_or_create(**validated_data['translation'])
        link = Link.objects.create(base=base, translation=translation, user=validated_data['user'])
        return link


class PaginationGetLinkSerializer(serializers.ModelSerializer):
    base = serializers.CharField(source='base.word')
    translations = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = ['base', 'translations']

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_translations(self, obj):
        return (Link.objects.filter(base=obj.base, translation__language=obj.translation.language)
                .values_list('translation__word', flat=True))


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'
