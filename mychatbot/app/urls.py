# -*- coding: utf-8 -*-
__author__ = 'adityasharma'
from django.conf.urls import url, patterns
from . import views

urlpatterns = [
    url(r'^$', views, name='')
]