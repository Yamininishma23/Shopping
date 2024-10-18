from django.urls import path
from . import views
from django.conf import settings  # Import settings
from django.conf.urls.static import static  # Import static to serve media files

urlpatterns = [
    path('', views.home),  # Your home view
]

# Add this part to serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
