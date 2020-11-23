from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from menu1 import settings
from app import views

urlpatterns = [
    path('restoran/', admin.site.urls),
    path('', views.product_list, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
