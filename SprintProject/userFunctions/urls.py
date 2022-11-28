from django.urls import path
from userFunctions import views
urlpatterns = [
    path('cadastro', views.registerView, name='cadastro'),
    path('profile', views.userProfile, name='profile'),
    path('login', views.userLogin, name='login'),
]
