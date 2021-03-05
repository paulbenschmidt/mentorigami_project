from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from core import urls as core_urls
from app_search import urls as search_urls
from profiles import urls as profiles_urls
from users import urls as users_urls

app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^/', include(core_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^profiles/', include(profiles_urls)),
    url(r'^users/', include(users_urls)),
]
