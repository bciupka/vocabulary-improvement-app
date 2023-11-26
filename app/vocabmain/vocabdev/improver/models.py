from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings


class Language(models.Model):
    language_pol = models.CharField(max_length=100, unique=True)
    language_eng = models.CharField(max_length=100, unique=True)
    symbol = models.SlugField(max_length=3, unique=True)

    def __str__(self):
        return f'{self.language_eng} language'


class Word(models.Model):
    word = models.CharField(max_length=255)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.word}'

    def clean(self):
        if not self.word.islower():
            self.word = self.word.lower()
        if Word.objects.filter(language=self.language, word=self.word).exists():
            raise ValidationError({'word': 'Duplicated word for language'})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Link(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    base = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='base')
    translation = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='transation')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('user', 'base', 'translation'), name='link_uniqueness')
        ]

    def __str__(self):
        return f'{self.user.username} - {self.base} {self.translation.language.symbol}'
