from django.contrib.auth.models import User
from django import forms
from .models import Blog

class CreateBlog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content']

class UpdateBlog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=['title','content']

class DeleteBlog(forms.ModelForm):
    class Meta:
        model=Blog
        fields=[]
