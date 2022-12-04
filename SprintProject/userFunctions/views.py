from django.shortcuts import render, redirect
from userFunctions.forms import registerForm
from django.contrib.auth import logout, authenticate, login
from datetime import datetime
import calendar

from django.contrib.auth.decorators import login_required

from companyTeam.models import compTeamModel
# Create your views here.

def registerView(request):

    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            print('valido')
            form.save()
            return redirect('/profile')
        else:
            return redirect('/cadastro')
    else:
        form = registerForm

    return render(request, 'register/registration.html', {'form':form})

@login_required(login_url='/login')
def userProfile(request):
    now = datetime.now()
    current_month = now.month
    year = now.year
    month_name = calendar.month_name[current_month]
    
    user_teams = compTeamModel.objects.filter(manager=request.user.profile)

    if user_teams:

        context = {"month_name": month_name,
        "year":year, "times":user_teams}
    else:
        context = {"month_name": month_name,
        "year":year}
    
    return render(request, 'profile/profile.html', context)


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            return redirect('/login')
    else:
        pass

    return render(request, 'login/login.html')

def logoutView(request):
    logout(request)


