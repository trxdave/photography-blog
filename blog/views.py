from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from.models import Category, Post, Photo, LandscapeImage
from django.contrib.auth.views import LoginView, LogoutView
from.forms import LandscapeImageForm, PostForm

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
    if request.method == 'POST':
        form = LandscapeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landscape_image_list')
    else:
        form = LandscapeImageForm()
    return render(request, 'upload_landscape_image.html', {'form': form})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            category_name = request.POST.get('category')
            if category_name == 'Landscape':
                category = Category.objects.get(name='Landscape')
            elif category_name == 'Portrait':
                category = Category.objects.get(name='Portrait')
            elif category_name == 'Wildlife':
                category = Category.objects.get(name='Wildlife')
            elif category_name == 'Street':
                category = Category.objects.get(name='Street')
            elif category_name == 'Macro':
                category = Category.objects.get(name='Macro')
            else:
                return render(request, 'errors/404.html')

            post = Post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                image=form.cleaned_data['image'],
                category=category
            )
            post.save()
            return redirect('blog_view')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def landscape_image_list(request):
    images = LandscapeImage.objects.all()
    return render(request, 'landscape_image_list.html', {'images': images})

def handler400(request, exception):
    return render(request, 'errors/400.html')

def handler403(request, exception):
    return render(request, 'errors/403.html')

def handler404(request, exception):
    return render(request, 'errors/404.html')

def handler500(request):
    return render(request, 'errors/500.html')