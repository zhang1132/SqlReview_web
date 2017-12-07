# -*- coding:utf-8 -*-
from django.conf.urls import include, url
from inception import views

urlpatterns = [
    url(r'^$', views.inception),
    url(r'^index$', views.inception),
    url(r'^inception$', views.inception),
    url(r'^sqlhandle$', views.sqlhangle),
    url(r'^rollback$', views.rollback),

]