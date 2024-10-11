from django.db import models

from files.utils import UniqueNameFileField


class File(models.Model):
    '''Модель файла.'''

    title = models.CharField(
        verbose_name='Название',
        max_length=150,
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
    )
    file = UniqueNameFileField(
        verbose_name='Файл',
        upload_to='uploads'
        )
    create_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        db_table = 'file'
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'
        ordering = ('id', )

    def __str__(self):
        return self.title
