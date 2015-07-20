from . import views
from django.conf.urls import url, include

urlpatterns = [
        url('^$',views.index, name='visdemo.index'),
        url('^svg/$', views.svg_demo, name='visdemo.svg'),
]
