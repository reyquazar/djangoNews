from django.urls import path
from .views import article_detail, home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('article/<int:article_id>/', article_detail, name='article_detail'),
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
