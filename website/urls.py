from django.contrib import admin
from django.conf import settings
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
