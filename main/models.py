# coding=utf-8
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import smart_unicode


class Art(models.Model):
    class Meta:
        verbose_name_plural = 'Добавление фотографий'
        verbose_name = 'Добавление фотогафий'

    title = models.CharField(max_length=255, verbose_name='Название фотографии')
    images = models.ImageField(upload_to='images/arts', verbose_name='Главная картинка')
    description = models.TextField(verbose_name='Описание фотографии')
    type_of_art = models.CharField(max_length=255, verbose_name='Тип')

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class ArtImages(models.Model):
    class Meta:
        verbose_name_plural = 'Дополнительные фотографии'
        verbose_name = 'Дополнительные фотографии'

    art = models.ForeignKey(Art, verbose_name='Выберите Картинку')
    image = models.ImageField(upload_to='images/art', verbose_name='Загрузить дополниьельные картинки')

    def __unicode__(self):
        return smart_unicode(self.art.title)
