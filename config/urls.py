from django.conf.urls import include, url

from app_home import views as home_views
from app_search import urls as search_urls
from app_settings import urls as settings_urls

urlpatterns = [
    url(r'^$', home_views.home_page, name='home'),
    url(r'^search_results/', include(search_urls, namespace='search')),
    url(r'^settings/', include(settings_urls, namespace='settings'))
]
