from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Photo, Category
from .forms import PhotoForm, ContactForm
import cloudinary.uploader as uploader

def homepage_view(request):
    return render(request, 'blog/homepage.html')

def blog_view(request):
    photos = Photo.objects.all()
    return render(request, 'blog/blog.html', {'photos': photos})

def viewPhoto(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'blog/photo_detail.html', {'photo': photo})

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

def blog(request):
    photo_list = Photo.objects.all()
    paginator = Paginator(photos_list, 6)
    page_number = request.GET.get('page')
    photos = paginator.get_page(page_number)
    return render(request, 'blog/blog.html', {'photos': photos})

def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'blog/photo_list.html', {'photos': photos})

def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(render, 'blog/photo_detail.html', {'photo': photo})

@login_required
def edit_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'blog/edit_photo.html', {'form': form})

@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == 'POST':
        photo.delete()
        return redirect('photo_list')
    return render(request, 'blog/confirm_delete.html', {'photo': photo})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')

def category_view(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    photos = Photo.objects.filter(categoryimage=category)
    return render(request, f'blog/{category_name}.html', {'photos': photos, 'category': category})

def landscape_photos(request):
    landscape_photos = Photo.objects.filter(categoryimage__name='1')
    return render(request, 'blog/landscape.html', {'photos': landscape_photos})

def portrait_photos(request):
    portrait_photos = Photo.objects.filter(categoryimage__name='2')
    return render(request, 'blog/portrait.html', {'photos': portrait_photos})

def wildlife_photos(request):
    wildlife_photos = Photo.objects.filter(categoryimage__name='3')
    return render(request, 'blog/wildlife.html', {'photos': wildlife_photos})

def street_photos(request):
    street_photos = Photo.objects.filter(categoryimage__name='4')
    return render(request, 'blog/street.html', {'photos': street_photos})

def macro_photos(request):
    marco_photos = Photo.objects.filter(categoryimage__name='5')
    return render(request, 'blog/macro.html', {'photos': macro_photos})

class PhotoListView(ListView):
    model = Photo
    template_name = 'blog/photo_list.html'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'blog/photo_detail.html'

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()  # Assume you handle sending email inside the form's save method
        return redirect('success')
    return render(request, 'blog/contact.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html')

def success(request):
    return render(request, 'success.html')

# Error Handlers
def handler400(request, exception):
    return render(request, 'errors/400.html')

def handler403(request, exception):
    return render(request, 'errors/403.html')

def handler404(request, exception):
    return render(request, 'errors/404.html')

def handler500(request):
    return render(request, 'errors/500.html')