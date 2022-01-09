from django.contrib import admin
from django.urls import include
from django.urls import path
from transactions import api

urlpatterns = [
    path('test', api.Test.as_view(),name="test"),
]
