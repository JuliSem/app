from django.http import HttpResponse
from rest_framework import mixins, viewsets
from rest_framework.decorators import action

from files.models import File
from files.serializers import (
    FileListSerializer,
    FileSerializer
)


class FileViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    """ViewSet модели File."""

    queryset = File.objects.all()

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return FileListSerializer
        return FileSerializer

    @action(
        detail=True, methods=['get']
    )
    def download(self, request, pk=None):
        download_file = File.objects.get(id=pk)
        file_path = download_file.file.path
        with open(file_path, 'rb') as f:
            response = HttpResponse(
                f.read(),
                content_type='application/octet-stream'
                )
            response['Content-Disposition'] = f'attachment; filename="{download_file.file.name}"'
        return response
