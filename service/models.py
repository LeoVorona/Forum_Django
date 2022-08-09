from ast import Delete
from email.mime import image
from pydoc import describe
from django.db import models

class Post(models.Model):

    title = models.CharField(verbose_name='Название', max_length=100)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    image = models.ImageField(verbose_name='Картинка')
    created_at = models.DateField(verbose_name="Дата создания",auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата изменения' ,auto_now = True)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateField(verbose_name="Дата создания",auto_now_add=True)

    def __str__(self):
        return f'{self.description}'