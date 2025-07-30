from django.urls import path
from . import views

app_name = 'simulation'

urlpatterns = [
    path('', views.index, name='index'),
    path('start/', views.start_simulation, name='start_simulation'),
    path('result/<int:simulation_id>/', views.simulation_result, name='simulation_result'),
] 