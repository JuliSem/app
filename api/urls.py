from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers

from files.views import FileViewSet

router = routers.DefaultRouter()

router.register(r'files', FileViewSet, basename='files')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'v1/schema/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger'
    ),
]
