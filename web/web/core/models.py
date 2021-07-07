from django.db import models


class Task(models.Model):

    date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, verbose_name='Название')
    full_text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
