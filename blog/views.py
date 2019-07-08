from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.decorators import login_required
from .blog_form import CreateBlog,UpdateBlog,DeleteBlog
from django.contrib.auth.models import User

# Create your views here.
@login_required
def home(request):
    blogs=Blog.objects.all()
    return render(request,"blog/home.html",{"blogs":blogs})

@login_required
def create(request):
    if(request.method=="POST"):
        blog_form=CreateBlog(request.POST)
        if(blog_form.is_valid()):
            x=Blog(author=User.objects.get(id=request.user.pk),title=request.POST['title'],content=request.POST['content'])
            #agar html mein crispy lga doge toh in title there will be html added , there use request.POST['title']
            x.save()
            messages.success(request,f'Blog is created')
            return redirect('user_blogs')
    else:
        blog_form=CreateBlog()
    return render(request,'blog/create.html',{'blog_form':blog_form})

@login_required
def user_blogs(request):
    blogs=Blog.objects.filter(author=request.user)
    return render(request,'blog/user_blogs.html',{'blogs':blogs})

# @login_required
def delete(request,blog_id):
    blogs=Blog.objects.get(id=blog_id)
    if(blogs.author !=request.user):
        messages.warning(request,f"You cant delete other's blog")
        return redirect('user_blogs')
    if(request.method=="POST"):
        blog_form=DeleteBlog(request.POST)
        if(blog_form.is_valid()):
            blogs.delete()
            messages.warning(request,f'You have deleted a blog')
            return redirect('user_blogs')
    else:
        # print("hi")
        blog_form=DeleteBlog()
    return render(request,'blog/delete.html',{'blog_form':blog_form})


@login_required
def update(request,blog_id):
    blogs=Blog.objects.get(id=blog_id)
    if(blogs.author !=request.user):
        messages.warning(request,f"You cant edit other's blog")
        return redirect('user_blogs')
    if(request.method=="POST"):
        blog_form=UpdateBlog(request.POST,instance=blogs)
        if(blog_form.is_valid()):
            blog_form.save()
            messages.success(request,f'Blog is updated')
            return redirect('blog_home')
    else:
        blog_form=UpdateBlog(instance=blogs)
    return render(request,'blog/update.html',{'blog_form':blog_form})
