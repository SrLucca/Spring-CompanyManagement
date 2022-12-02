from django.urls import path
from employeesCalendar import views


urlpatterns = [
    path('calendario/<int:year>/<str:month>/', views.calendarView, name='calendar'),
]
