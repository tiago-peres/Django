from django.conf.urls import url
from . import views

# Create your urls here.
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^submit', views.submit, name='submit')
]