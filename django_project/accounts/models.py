from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    favorites = models.ManyToManyField('pages.Book', related_name='favorites', blank=True)