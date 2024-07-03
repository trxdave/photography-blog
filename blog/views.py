from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Category, Post, Photo
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LandscapeImageForm
from .models import LandscapeImage

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

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_view')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def category_view(request, category):
    category_obj = Category.objects.filter(name=category).first()
    if category_obj:
        photos = Photo.objects.filter(category=category_obj)
        return render(request, 'blog/category.html', {'photos': photos, 'category': category})
    else:
        return render(request, 'errors/404.html')

def upload_landscape_image(request):
    if request.method == 'Post':
        form = LandscapeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landscape_image_list')
    else:
        form = LandscapeImageForm()
    return render(request, 'upload_landscape_image.html', {'form': form})

def landscape_image_list(request):
    images = LandscapeImage.objects.all()
    return render(request, 'landscape_image_list.html', {'images': images})


def handler400(request, exception):
    """ Error Handler 400 - Bad Request """
    return render(request, "errors/400.html", status=400)


def handler403(request, exception):
    """ Error Handler 403 - Forbidden """
    return render(request, "errors/403.html", status=403)


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Error Handler 500 - Internal Server Error """
    return render(request, "errors/500.html", status=500)