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
    path('register_user/',views.register_user,name="register_user"),
    path('verify_otp/<id>',views.verify_otp,name="verify_otp"),
    path('login_user',views.login_user,name="login_user"),
    path('forgot_password/',views.forgot_password,name="forgot_pasword"),
    path('forgot_verify_otp/<id>',views.forgot_verify_otp,name="forgot_verify_otp"),
    path('updated_password/<id>',views.update_password,name="update_password"),
    path('list_view/',views.TeamsListView.as_view(),name="list_view"),
    path('detail_view/<pk>',views.TeamsDetailView.as_view(),name="detail_view"),
    path('update_view/<pk>',views.TeamsUpdateView.as_view(),name="update_view"),
    path('create_view/',views.TeamsCreateView.as_view(),name="create_view"),
    path('delete_view/<pk>',views.TeamsDeleteView.as_view(),name="delete_view")

]

rest_urls = [
    path('hello_world',views.Hello_world),
    path('teams',views.teams_get_post_api_view),
    path('teams/<id>',views.teams_get_put_delete_api_view),
    path('cls_teams_api/',views.TeamClsAPIView.as_view()),
    path('cls_teams_api/<id>',views.TeamClsAPIUpdateView.as_view()),
    path('cls_list_create_view/',views.TeamListCreateView.as_view()),
    path('cls_retrieve_view/<pk>/',views.TeamRetrievewView.as_view()),
    path('cls_retrieve_update_destroy_view/<pk>/',views.TeamRetrieveUpdateDestroyView.as_view())
]

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'viewset_teams',views.TeamsViewSet,basename='Teams')
urlpatterns = urlpatterns+rest_urls + router.urls