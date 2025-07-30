from django.urls import path
from . import views

app_name = 'restapi'

urlpatterns = [
    path('', views.index, name='index'),
    path('characters/', views.character_list, name='character_list'),
    path('support-cards/', views.support_card_list, name='support_card_list'),
    path('skills/', views.skill_list, name='skill_list'),
] 