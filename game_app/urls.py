from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('charactercreation', views.success),
    path('createcharacter', views.create_character),
    path("home/<int:user_id>", views.home_page),
    path("forest/<int:user_id>", views.forest_page),
    path("forest_battle_scene/<int:user_id>", views.forest_battle_page),
    path("attack/<int:user_id>", views.attack),
    path("attack/win/<int:user_id>", views.win_page)
    
]