from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout"),
    path('room/<str:id>', views.room, name="room"),
    path('create_room', views.create_room, name="create_room"),
    path('update_room/<str:id>', views.update_room, name="update_room"),
    path('delete_room/<str:id>', views.delete_room, name="delete_room"),
]
