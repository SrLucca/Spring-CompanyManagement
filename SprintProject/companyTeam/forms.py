from django.forms import ModelForm
from companyTeam.models import compTeamModel, employessActivities

class createCompTeam(ModelForm):

    class Meta:
        model = compTeamModel
        fields = ['nome', 'email_profissional', 'imagem_do_time', 'horario_de_atividade']

class createActivities(ModelForm):

    class Meta:
        model = employessActivities
        fields = ['integrante', 'atividade', 'prazo_final']
