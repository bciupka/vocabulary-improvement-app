from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.validators import RegexValidator
from django.db.models.functions import Lower, Random
import random


class SelfValidatingModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)


class Language(SelfValidatingModel):
    language_pol = models.CharField(max_length=100, unique=True)
    language_eng = models.CharField(max_length=100, unique=True)
    symbol = models.SlugField(max_length=3, unique=True)

    def __str__(self):
        return f'{self.language_eng} language'


class Word(SelfValidatingModel):
    WordValidator = RegexValidator(r'^[a-zA-Z]*$','Only letters allowed')

    word = models.CharField(max_length=255, validators=[WordValidator])
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('word', 'language'), name='word_uniqueness')
        ]

    def __str__(self):
        return f'{self.word}'

    def clean(self):
        if not self.word.islower():
            self.word = self.word.lower()


class Link(SelfValidatingModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    base = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='base')
    translation = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='transation')
    random_nr = models.DecimalField(max_digits=4, decimal_places=3, default=0.001, null=True, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user', 'base', 'translation'), name='link_uniqueness')
        ]

    def __str__(self):
        return f'{self.user.username} - {self.base} {self.translation.language.symbol}'

    def clean(self):
        if self.base.language == self.translation.language:
            raise ValidationError({'link': 'Same language in both words'})
