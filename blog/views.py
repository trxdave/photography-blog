from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LogoutView, LoginView
from blog.models import Photo, Category
from .forms import PhotoForm, ContactForm
from cloudinary.uploader import upload
import cloudinary

def homepage_view(request):
    return render(request, 'blog/homepage.html')

@login_required
def add_photo(request, category=None):
    if category is None:
        return redirect('select_category')
    else:
        if request.method == 'POST':
            form = PhotoForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('blog')
            else:
                return render(request, 'blog/add_photo.html', {'form': form})
        else:
            form = PhotoForm()
    return render(request, 'blog/add_photo.html', {'form': form})

@login_required
def select_category(request):
    categories = Category.objects.all()
    return render(request, 'blog/select_category.html', {'categories': categories})

def blog(request):
    photos = Photo.objects.all()
    return render(request, 'blog.html', {'photos': photos})

@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'blog/photo_list.html', {'photos': photos})

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

def signout_view(request):
    return LogoutView.as_view(next_page='homepage')(request)

def blog_view(request):
    photos = Photo.objects.all()
    return render(request, 'blog/blog.html', {'photos': photos})

class PhotoListView(ListView):
    model = Photo
    template_name = 'blog.html'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'

class CategoryDetailView(DetailView):
    model = Category
    context_object_name = 'category'

def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    photos = category.category_photos.all()
    return render(request, 'category_detail.html', {'category': category, 'photos': photos})

def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def landscape_photos(request):
    photos = Photo.objects.all()
    return render(request, 'landscape.html', {'photos': photos})

def portrait_photos(request):
    photos = Photo.objects.all()
    return render(request, 'portrait.html', {'photos': photos})

def wildlife_photos(request):
    photos = Photo.objects.all()
    return render(request, 'wildlife.html', {'photos': photos})

def street_photos(request):
    photos = Photo.objects.all()
    return render(request, 'street.html', {'photos': photos})

def macro_photos(request):
    photos = Photo.objects.all()
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
    return render(request, 'blog/add_photo.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nMessages: {message}',
                '56hq2ig9@students.codeinstitute.net',
                ['56hq2ig9@students.codeinstitute.net'],
                fail_silently=False,
            )
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'blog/contact.html', {'form': form})

def success(request):
    return render(request, 'success.html')

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