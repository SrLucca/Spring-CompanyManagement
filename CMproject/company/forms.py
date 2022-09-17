from django import forms
from company.models import companyModel

class companyRegister(forms.ModelForm):

    class Meta:
        model = companyModel
        fields = [
            "nome",
            "cnpj",
            "email",
            "telefone",
            "endereco"
        ]