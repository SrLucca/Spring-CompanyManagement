from django.shortcuts import render, redirect
from companyTeam.forms import createCompTeam
from companyTeam.models import compTeamModel
from django.http import QueryDict

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
