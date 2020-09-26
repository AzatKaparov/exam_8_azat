from django.contrib.auth.models import User
from django.db import models

DEFAULT_CATEGORY = 'other'

CATEGORY_CHOICES = [
    (DEFAULT_CATEGORY, 'Разное'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('car', 'Для машины'),
    ('wash', 'Чистящие средства'),
    ('tools', 'Инструменты'),
    ('toys', 'Игрушки')
]

MARK_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
]


class Product(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Название')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, null=False, blank=False,
                                default=DEFAULT_CATEGORY, verbose_name='Категория')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка')

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return f'{self.name} - {self.category}'


class Review(models.Model):
    author = models.ForeignKey('accounts.Profile', related_name='author_profile', on_delete=models.CASCADE,
                               verbose_name='Автор')
    product = models.ForeignKey('webapp.Product', related_name='product_review', on_delete=models.CASCADE,
                                verbose_name='Товар')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст')
    mark = models.IntegerField(choices=MARK_CHOICES, null=False, blank=False, verbose_name='Оценка')

    class Meta:
        verbose_name_plural = 'Оценки'
        verbose_name = 'Оценка'

    def __str__(self):
        return f'{self.author} - {self.product.name} - {self.mark}'




