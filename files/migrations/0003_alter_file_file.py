# Generated by Django 5.1.1 on 2024-10-10 14:07

import files.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_alter_file_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=files.models.UniqueNameFileField(upload_to='uploads', verbose_name='Файл'),
        ),
    ]
