import imp
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path,include,re_path
from django.views.static import serve


urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root: settings.MEDIA_ROOT'}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
