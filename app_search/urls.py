from django.conf.urls import url

from . import views

# Namespace for app
app_name = 'search'

urlpatterns = [
    url(r'^$', views.search_results, name='search_results'),
]
