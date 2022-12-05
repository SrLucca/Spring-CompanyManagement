from django.urls import path
from companyTeam import views

urlpatterns = [
    path('create-company-team', views.createTeam, name='create-team'),
    path('times/<str:nome>', views.teamView, name='team-view'),
]
