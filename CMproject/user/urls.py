from django.urls import path
from .import views


urlpatterns = [

    path('register/', views.userRegister, name="register"),
    path('login/', views.userLogin, name="login"),
    path('edit-profile/', views.editProfileView, name="edit-Profile"),
    path('profile/', views.profileView, name="profile"),

]