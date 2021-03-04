from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path

from app_home import urls as home_urls
from app_search import urls as search_urls
from app_settings import urls as settings_urls
from users import urls as users_urls

app_name = 'config'

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', include(home_urls)),
    url(r'^search/$', include(search_urls)),
    url(r'^settings/$', include(settings_urls)),
    url(r'^users/', include(users_urls)),
]
