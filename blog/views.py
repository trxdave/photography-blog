from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Photo
from django.contrib.auth.views import LoginView, LogoutView

class PhotoListView(ListView):
    model = Photo
    template_name = 'blog.html'
    context_object_name = 'post_list'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'blog/photo_detail.html'

class SignoutView(LogoutView):
    template_name = 'account/logout.html'
    next_page = '/'

class SigninView(LoginView):
    template_name = 'blog/signin.html'

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

@login_required
def homepage_view(request):
    return render(request, 'blog/homepage.html')

def about(request):
    return render(request, 'blog/about.html')

def blog_view(request):
    return render(request, 'blog/blog.html')