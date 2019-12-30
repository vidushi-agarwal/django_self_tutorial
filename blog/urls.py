from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name="blog_home"),
    path('create/',views.create,name="blog_create"),
    path('user_blogs/',views.user_blogs,name="user_blogs"),
    path('user_blogs/delete/<int:blog_id>/', views.delete, name="blog_delete"),
    path('user_blogs/update/<int:blog_id>/', views.update, name="blog_update"),
]
