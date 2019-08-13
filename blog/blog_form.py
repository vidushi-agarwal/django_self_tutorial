from django.contrib.auth.models import User
from django import forms
from .models import Blog
// yahaan sb jagah model affect ho rha h islie modelform
// aur separate model islie nhi bnaya coz dbtable nhi bnani bas table blog mein changes krne h
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
