# app/urls.py
from django.conf.urls import url
from . import views

# Create your urls here.
urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^test/$', views.test, name='test'),
  url(r'^profile/$', views.profile, name='profile')
]