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
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'blog/add_photo.html', {'form': form})

@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'blog/photo_list.html', {'photos': photos})

@login_required
def create_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'blog/create_photo.html', {'form': form})

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

def category_view(request, category):
    if category == 'landscape':
        photos = Photo.objects.filter(category__slug='landscape')
    elif category == 'portrait':
        photos = Photo.objects.filter(category__slug='portrait')
    elif category == 'wildlife':
        photos = Photo.objects.filter(category__slug='wildlife')
    elif category == 'treet':
        photos = Photo.objects.filter(category__slug='street')
    elif category == 'acro':
        photos = Photo.objects.filter(category__slug='macro')
    else:
        # Handle unknown categories
        return HttpResponseNotFound('Category not found')

    return render(request, 'blog/category.html', {'photos': photos})

def landscape_view(request):
    photos = Photo.objects.filter(category='landscape')
    return render(request, 'blog/category.html', {'photos': photos})

def upload_landscape_image(request):
    if request.method == 'POST':
        form = LandscapeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('blog/photo_list.html')
    else:
        form = LandscapeImageForm()
    return render(request, 'blog/landscape.html', {'form': form})

def portrait_view(request):
    photos = Photo.objects.filter(category='portrait')
    return render(request, 'blog/category.html', {'photos': photos})

def upload_portrait_image(request):
    if request.method == 'POST':
        form = PortraitImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('blog/photo_list.html')
    else:
        form = PortraitImageForm()
    return render(request, 'blog/portrait.html', {'form': form})

def wildlife_view(request):
    photos = Photo.objects.filter(category='wildlife')
    return render(request, 'blog/category.html', {'photos': photos})

def upload_wildlife_image(request):
    if request.method == 'POST':
        form = WildlifeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('blog/photo_list.html')
    else:
        form = WildlifeImageForm()
    return render(request, 'blog/wildlife.html', {'form': form})

def street_view(request):
    photos = Photo.objects.filter(category='street')
    return render(request, 'blog/category.html', {'photos': photos})

def upload_street_image(request):
    if request.method == 'POST':
        form = StreetImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('blog/photo_list.html')
    else:
        form = StreetImageForm()
    return render(request, 'blog/street.html', {'form': form})

def macro_view(request):
    photos = Photo.objects.filter(category='macro')
    return render(request, 'blog/category.html', {'photos': photos})

def upload_macro_image(request):
    if request.method == 'POST':
        form = MacroImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('blog/photo_list.html')
    else:
        form = MacroImageForm()
    return render(request, 'blog/macro.html', {'form': form})

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
    return render(request, 'about.html')

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