from django.urls import path
from django.conf.urls.static import static
from .views import projects, experience
from django.conf import settings

urlpatterns = [
      path('', projects, name="projects"),
      path("experience", experience, name="experience"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)