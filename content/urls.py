from django.urls import path
from django.conf.urls.static import static
from .views import projects
from django.conf import settings

urlpatterns = [
      path('', projects, name="projects")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)