from django.db import models

# Create your models here.

class companyModel(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=False)
    cnpj = models.CharField(max_length=14, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    telefone = models.CharField(max_length=11, help_text="Ex: 11999999999")
    endereco = models.TextField(blank=False, null=False, help_text="Rua,numero,cep,complemento etc..")