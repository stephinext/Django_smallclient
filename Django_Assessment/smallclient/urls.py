from django.contrib import admin
from django.urls import path
from .views import CreateClient,ViewClient,View,ListClient


urlpatterns = [
    path('create', CreateClient.as_view(),name='create_client'),
    path('<int:pk>/', ViewClient.as_view(),name='view_client'),
    path('', ListClient.as_view(), name='list_clients'),
]
