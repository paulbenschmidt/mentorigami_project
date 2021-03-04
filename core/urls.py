from django.conf.urls import url
from core import views

app_name = 'core'

urlpatterns = [
    url(r'', views.home, name='home'),
]
