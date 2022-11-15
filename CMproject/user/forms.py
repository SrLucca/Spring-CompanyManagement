from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser

from django import forms

from user.models import Profile

class registerForm(UserCreationForm):

    username = forms.CharField(required=True,widget=forms.TextInput(attrs={'placeholder':'Não deve conter espaços','class':'u-border-1 u-border-custom-color-2 u-input u-input-rectangle u-radius-4 u-text-custom-color-2 u-input-1'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class':'u-border-1 u-border-custom-color-2 u-input u-input-rectangle u-radius-4 u-text-custom-color-2 u-input-3'}))
    nome_completo = forms.CharField(required=True,widget=forms.TextInput(attrs={'class':'u-border-1 u-border-custom-color-2 u-input u-input-rectangle u-radius-4 u-text-custom-color-2 u-input-1'}))
    cpf = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'u-border-1 u-border-custom-color-2 u-input u-input-rectangle u-radius-4 u-text-custom-color-2 u-input-2'}))
    telefone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'u-border-1 u-border-custom-color-2 u-input u-input-rectangle u-radius-4 u-text-custom-color-2 u-input-2'}))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={'type':'password','class':'u-border-1 u-border-custom-color-2 u-input u-input-rectangle u-radius-4 u-text-custom-color-2 u-input-1'}))
    
    class Meta:
        model = CustomUser
        fields = ['username','email', 'nome_completo', 'cpf', 'telefone', 'password1']

    def __init__(self, *args, **kwargs):
        super(registerForm, self).__init__(*args, **kwargs)
        del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None


class ProfileForm(forms.ModelForm):

    profile_image = forms.ImageField(widget = forms.FileInput(attrs = {'onchange': "upload_img(this);"}))

    class Meta:
        model = Profile
        fields = [
            'profile_image',
            ]