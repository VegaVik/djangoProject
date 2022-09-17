from audioop import reverse
from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.urls import reverse

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Category (models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name = 'Наименование категорий')

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
