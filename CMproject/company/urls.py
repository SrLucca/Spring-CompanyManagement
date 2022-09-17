from django.urls import path
from .import views


urlpatterns = [

    path('register-company/', views.registerCompanyView, name="register-company"),

]