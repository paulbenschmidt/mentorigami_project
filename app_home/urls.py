from django.conf.urls import url
from app_home import views

app_name = 'home'

urlpatterns = [
    url(r'', views.home_page, name='home_page'),
]
