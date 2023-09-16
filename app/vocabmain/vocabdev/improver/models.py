from django.db import models


class VocabUser(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} User'


class Polish(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.word} Word'
