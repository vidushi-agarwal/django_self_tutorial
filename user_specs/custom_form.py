from django import forms#(here we have to inherit ModelForm from forms like in models Model)
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomReg(UserCreationForm):    #inheriting UserCreationForm
    email=forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        
class RegisterDp(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dp']


class UpdateDp(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['dp']

class UpdateReg(forms.ModelForm): #not dp and you cant update password and dont inherit UserCreationForm as we are updating UserCreationForm
    class Meta:
        model = User
        fields = ['username', 'email']
