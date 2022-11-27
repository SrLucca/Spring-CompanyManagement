from django.shortcuts import render, redirect
from userFunctions.forms import registerForm
from django.contrib.auth import logout
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

def userProfile(request):
    return render(request, 'profile/profile.html')

def logoutView(request):
    logout(request)


