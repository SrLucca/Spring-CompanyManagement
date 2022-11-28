from django.shortcuts import render, redirect
from userFunctions.forms import registerForm
from django.contrib.auth import logout, authenticate, login
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


