from django.conf.urls import url

from . import views

app_name = 'products'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/like/$', views.do_like, name='like')
]