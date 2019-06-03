from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    my_user=models.OneToOneField(User,on_delete=models.CASCADE)
    dp=models.ImageField(default='profile_pic/default.jpg',upload_to='profile_pic/')
    def __str__(self):#to rename all the images by username
        return f'{self.my_user.username} dp'
