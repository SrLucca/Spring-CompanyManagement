from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/login')
def calendarView(request, month, year):

    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year
    return render(request,'calendar.html',{
        "year":year,
        "month":month,
        "month_number":month_number,
        "cal": cal,
        "current_year":current_year
    })