from django.urls import path, include
from .views import file_list, upload_file, delete_file
from rest_framework.routers import DefaultRouter
from .views import UploadedFileViewSet

router = DefaultRouter()
router.register(r'files', UploadedFileViewSet)


urlpatterns = [
    path('files/', file_list, name='file_list'),
    path('upload/', upload_file, name='upload_file'),
    path('delete<int:pk>/', delete_file, name='delete_file'),
    path('', include(router.urls)),
]

