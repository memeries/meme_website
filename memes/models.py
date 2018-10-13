from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

from django.utils import timezone


class Type(models.Model):
    name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name


class Memes(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    link = models.URLField(verbose_name='link')
    thumbnail = models.URLField(verbose_name='thumbnail')
    transcribe = models.TextField()
    likes = models.IntegerField(default=0)
    type = models.ManyToManyField(Type, blank=True)
    nsfw = models.BooleanField()
    date_added = models.DateTimeField(default=timezone.now)
