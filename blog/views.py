from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LogoutView, LoginView
from blog.models import Photo, Category
from .forms import PhotoForm, LandscapeImageForm, PortraitImageForm, WildlifeImageForm, StreetImageForm, MacroImageForm
from cloudinary.uploader import upload

def homepage_view(request):
    return render(request, 'blog/homepage.html')

@login_required
def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            category = request.POST['category']
            if category == 'landscape':
                return render(request, 'landscape.html')
            elif category == 'portrait':
                return render(request, 'portrait.html')
            elif category == 'wildlife':
                return render(request, 'wildlife.html')
            elif category == 'treet':
                return render(request, 'treet.html')
            elif category == 'acro':
                return render(request, 'acro.html')
            else:
                return render(request, 'default.html')
    else:
        form = PhotoForm()
    return render(request, 'blog/add_photo.html', {'form': form})

@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'blog/photo_list.html', {'photos': photos})

@login_required
def category_photos(request, category_slug):
    category = get_object_or_404(Category,slug=category_slug)
    photos = Photo.objects.filter(category=category)
    return render(request, 'blog/category.html', {'photos': photos, 'category': category})

@login_required
def photo_detail(request, pk):
    photo = Photo.objects.get(pk=pk)
    return render(request, 'blog/photo_detail.html', {'photo': photo})

@login_required
def update_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'blog/update_photo.html', {'form': form})

@login_required
def delete_photo(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('photo_list')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')

def blog_view(request):
    photos = Photo.objects.all()
    return render(request, 'blog/blog.html', {'photos': photos})

class PhotoListView(ListView):
    model = Photo
    template_name = 'blog.html'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'

def category_view(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    photos = Photo.objects.filter(category=category)
    return render(request, 'blog/category.html', {'category': category, 'photos': photos})

def landscape_photos(request):
    category = Category.objects.get(name='Landscape')
    photos = Photo.objects.filter(category=category)
    return render(request, 'landscape.html', {'photos': photos})

def portrait_photos(request):
    category = Category.objects.get(name='Portrait')
    photos = Photo.objects.filter(category=category)
    return render(request, 'portrait.html', {'photos': photos})

def wildlife_photos(request):
    category = Category.objects.get(name='Wildlife')
    photos = Photo.objects.filter(category=category)
    return render(request, 'wildlife.html', {'photos': photos})

def street_photos(request):
    category = Category.objects.get(name='Street')
    photos = Photo.objects.filter(category=category)
    return render(request, 'street.html', {'photos': photos})

def macro_photos(request):
    category = Category.objects.get(name='Macro')
    photos = Photo.objects.filter(category=category)
    return render(request, 'macro.html', {'photos': photos})

class LogoutView(LogoutView):
    next_page = 'homepage'

class LoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'
    next_page = 'homepage'

def upload_image(request):
    if request.method == 'POST':
        result = upload(request.FILES['image'])
        photo = Photo(image=result['secure_url'], user=request.user)
        photo.save()
        return redirect('photo_list')
    return render(request, 'blog/upload_image.html')

def about(request):
    return render(request, 'blog/about.html')

def handler400(request, exception):
    """
    A view to handle HTTP 400 errors.

    request: The HTTP request object.
    exception: The exception that caused the error.

    Returns:
    A render of the 400 error template.
    """
    return render(request, 'errors/400.html')

def handler403(request, exception):
    """
    A view to handle HTTP 403 errors.

    request: The HTTP request object.
    exception: The exception that caused the error.

    Returns:
    A render of the 403 error template.
    """
    return render(request, 'errors/403.html')

def handler404(request, exception):
    """
    A view to handle HTTP 404 errors.

    request: The HTTP request object.
    exception: The exception that caused the error.

    Returns:
    A render of the 404 error template.
    """
    return render(request, 'errors/404.html')

def handler500(request):
    """
    A view to handle HTTP 500 errors.

    request: The HTTP request object.
    exception: The exception that caused the error.

    Returns:
    A render of the 500 error template.
    """
    return render(request, 'errors/500.html')