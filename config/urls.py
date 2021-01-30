from django.conf.urls import include, url

from home import views as home_views
from search import urls as search_urls
from settings import urls as settings_urls

urlpatterns = [
    url(r'^$', home_views.home_page, name='home'),
    url(r'^search_results/', include(search_urls, namespace='search')),
    url(r'^settings/', include(settings_urls, namespace='settings'))
]
