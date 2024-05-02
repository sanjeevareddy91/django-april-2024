from django.urls import path
from . import views

urlpatterns = [
    path('first_register/',views.first_register,name='first_register'),
    path('register/',views.register,name='register'),
    path('',views.teams_list,name='teams_list'),
    path('team/<id>',views.get_team,name="get_team"),
    path('delete_team/<id>',views.delete_team,name="delete_team"),
    path('registerteam_modelform/',views.registerteam_modelform,name="registerteam_modelform"),
    path('registerteam_form/',views.registerteam_form,name="registerteam_form"),
    path('register_user/',views.register_user,name="register_user")
]