from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class Profile(models.Model):
    user: AbstractUser = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Аватар')
    github = models.CharField(max_length=500, verbose_name='Ссылка на GitHub', blank=True)
    more = models.TextField(verbose_name='О себе', blank=True)

    def __str__(self):
        return self.user.get_full_name() + "'s Profile"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'