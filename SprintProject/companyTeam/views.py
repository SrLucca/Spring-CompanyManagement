from django.shortcuts import render, redirect, get_object_or_404
from companyTeam.forms import createCompTeam, createActi
from companyTeam.models import compTeamModel, employessActivities

from django.http import QueryDict

from django.contrib.auth.models import User

from django.forms import inlineformset_factory

# Create your views here.

def createTeam(request):
    
    if request.method == 'POST':
        nome = QueryDict.get(request.POST, key='nome')
        email = QueryDict.get(request.POST, key='email')
        imagem = QueryDict.get(request.FILES, key='imagem')
        horario = QueryDict.get(request.POST, key='horario')

        new_comp = compTeamModel.objects.create(nome=nome, email_profissional=email, imagem_do_time=imagem,
                                                manager=request.user.profile,horario_de_atividade=horario)

        new_comp.integrantes.add(request.user)
        new_comp.save()
        return redirect('/profile')
    else:
        pass
    
    return render(request, 'manager_page/create_team.html')


def teamView(request, nome):

    team = compTeamModel.objects.filter(nome=nome)

    context = {"team": team}

    return render(request, 'other/team_page.html', context)
    


def createAct(request, nome_time):
    
    if request.method == 'POST':
        form = createActi(request.POST)

        nome_atividade = form['atividade'].value()
        if form.is_valid():
            form.save()

                
        time = compTeamModel.objects.get(nome=nome_time)
        atividade = employessActivities.objects.get(atividade=nome_atividade)
        time.atividades.add(atividade)
        time.save()
        return redirect(f'/times/{nome_time}')
    form = createActi()

    context = {'form': form}
    return render(request, 'manager_page/create_act.html', context)