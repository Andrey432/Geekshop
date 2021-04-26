from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from mainapp import views as mainapp

urlpatterns = [
    path('', mainapp.main, name='home'),
    path('products/', include('mainapp.urls', namespace="products")),
    path('auth/', include('authapp.urls', namespace="auth")),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('contact/', mainapp.contact, name='contact'),
    path('admin/', include('adminapp.urls', namespace='adminapp')),
    path('django_admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [re_path(r'^__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
