from django.db import models
from django.contrib.auth.models import User
from userFunctions.models import Profile
# Create your models here.




class employessActivities(models.Model):
    empregado = models.OneToOneField(User, on_delete=models.CASCADE)
    atividade = models.CharField(max_length=500 ,blank=False, default="Fazer pedido...", null=False)
    prazo_maximo = models.DateField(auto_now=False, auto_now_add=False, )

    def __str__(self):
        return self.atividade

class compTeamModel(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, help_text="Nome da Equipe/Organização")
    email_profissional = models.EmailField(null=False, blank=False)
    imagem_do_time = models.ImageField(default='company.png', upload_to='companys/', null=True, blank=True)
    manager = models.OneToOneField(Profile, on_delete=models.CASCADE)
    integrantes = models.ManyToManyField(User)
    horario_de_atividade = models.TimeField(auto_now=False, auto_now_add=False)

    atividades = models.ManyToManyField(employessActivities)

    def __str__(self):
        return self.nome
