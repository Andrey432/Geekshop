from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mainapp import views as mainapp

urlpatterns = [
    path('', mainapp.main, name='home'),
    path('products/', include('mainapp.urls', namespace="products")),
    path('auth/', include('authapp.urls', namespace="auth")),
    path('basketapp/', include('basketapp.urls', namespace='basketapp')),
    path('contact/', mainapp.contact, name='contact'),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
