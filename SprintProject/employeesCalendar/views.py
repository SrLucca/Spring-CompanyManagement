from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
# Create your views here.

def calendarView(request, year, month):

    month_number = list(calendar.month_name).index(month)

    return render(request,'calendar.html',{
        "year":year,
        "month":month,
        "month_number":month_number
    })