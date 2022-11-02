from django.shortcuts import render, redirect
from user.forms import registerForm, ProfileForm

from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from user.models import CustomUser, CustomUserManager

from django.contrib import messages

# Create your views here.


def userRegister(request):

    if request.method == "POST":
        context = {'data': request.POST}
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha1 = request.POST.get('senha1')

        str(nome)
        nome.split(" ")

        try:
            new_user = CustomUserManager.create_user(self, email=email, password=senha1, cpf=cpf, telefone=telefone, nome_completo=nome)
            
            user = authenticate(request, email=email, password=senha1)

            login(request, user)


            return redirect(reverse('profile'))
        except:
            messages.add_message(request, messages.ERROR,
                                'Preencha todos os campos para poder se cadastrar!')
            return redirect('/register')
    else:
        form = registerForm()

    return render(request, 'pages/authentication/register.html', {'form':form})

def userLogin(request):

    if request.method == 'POST':
        context = {'data': request.POST}
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if not user:
            context = {'data': request.POST}
            messages.add_message(request, messages.ERROR,
                                'Credenciais inválidas, tente novamente.')
            return render(request, 'pages/authentication/login.html', context, status=401)

        login(request, user)


        return redirect(reverse('profile'))

    return render(request, "pages/authentication/login.html")

def userLogout(request):
    
    logout(request)
    
    return redirect('/') 

def profileView(request):

    if request.user.is_authenticated == True:
        return render(request, "pages/profile.html")
    else:
        return redirect('/')

def editProfileView(request):


    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Falha na edicao")
            return redirect('/profile')
    else:
        form = ProfileForm()

    return render(request, 'pages/edit-profile.html', {'form':form})