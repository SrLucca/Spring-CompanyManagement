from django.forms import ModelForm
from django import forms
from django.forms import widgets
from companyTeam.models import compTeamModel, employessActivities
class createCompTeam(ModelForm):

    class Meta:
        model = compTeamModel
        fields = ['nome', 'email_profissional', 'imagem_do_time', 'horario_de_atividade']


class createActi(ModelForm):

    prazo_maximo = forms.DateTimeField(widget = widgets.DateTimeInput(attrs = {'type': "datetime-local"}))
    class Meta:
        model = employessActivities

        fields = ['empregado', 'atividade','prazo_maximo']
