from django.conf.urls import url

from . import views

app_name = 'profiles'

urlpatterns = [
    url(r'^$', views.settings, name='settings'),
    url(r'^sign_in$', views.sign_in, name='sign_in'),
]
