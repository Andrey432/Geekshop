from django.contrib.auth.models import AbstractUser
from django.db import models


class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to="users_avatars", verbose_name="Аватар пользователя", blank=True)
    country = models.TextField(max_length=32, verbose_name="Страна", blank=True)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")

    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(auto_now_add=True, blank=True, null=True)
