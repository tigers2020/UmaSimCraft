from django.urls import path
from . import views

app_name = 'websocket'

urlpatterns = [
    path('', views.index, name='index'),
] 