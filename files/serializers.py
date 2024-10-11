from pathlib import Path
from rest_framework import serializers

from files.models import File


class FileSerializer(serializers.ModelSerializer):
    '''Serializer для создания файла.'''

    class Meta:
        model = File
        fields = ('title', 'description',  'file')


class FileListSerializer(FileSerializer):
    '''Serializer для получения файла/ файлов.'''

    origin_filename = serializers.SerializerMethodField()

    class Meta:
        model = File
        fields = ('origin_filename', 'file')

    def get_origin_filename(self, obj):
        origin_filename = Path(obj.file.name).name
        return origin_filename
