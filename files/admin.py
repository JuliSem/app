from django.contrib import admin

from files.models import File


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'description', 'file', 'create_date'
