from django.urls import path
from employeesCalendar import views


urlpatterns = [
    path('calendario/<str:month>/<int:year>/', views.calendarView, name='calendar'),
]
