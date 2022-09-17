from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms

from user.models import Profile

class registerForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["username","email","password1"]


class ProfileForm(forms.ModelForm):

    profile_image = forms.ImageField(widget = forms.FileInput(attrs = {'onchange': "upload_img(this);"}))

    class Meta:
        model = Profile
        fields = [
            'profile_image',
            ]