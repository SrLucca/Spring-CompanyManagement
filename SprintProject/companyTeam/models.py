from django.db import models
from django.contrib.auth.models import User
from userFunctions.models import Profile
# Create your models here.


class employessActivities(models.Model):
    integrante = models.OneToOneField(User, on_delete=models.CASCADE)
    atividade = models.TextField(blank=False, default="Fazer pedido...", null=False)
    prazo_final = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.integrante

class compTeamModel(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False, help_text="Nome da Equipe/Organização")
    email_profissional = models.EmailField(null=False, blank=False)
    imagem_do_time = models.ImageField(default='company.png', upload_to='companys/', null=True, blank=True)
    manager = models.OneToOneField(Profile, on_delete=models.CASCADE)
    integrantes = models.ManyToManyField(User)
    horario_de_atividade = models.TimeField(auto_now=False, auto_now_add=False)
    atividades = models.OneToOneField(employessActivities, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nome