# Generated by Django 5.1.1 on 2024-10-10 14:00

import files.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=files.models.UniqueNameFileField(upload_to='uploads'),
        ),
    ]
