from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LogoutView, LoginView
from blog.models import Photo, Category
from.forms import PhotoForm
from cloudinary.uploader import upload

def homepage_view(request):
    return render(request, 'homepage.html')

@login_required
def add_photo(request):
    """
    A view to handle post creation.

    Returns:
    A render of the add post template with a form, or a redirect to the post list if the form is valid.
    """
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            if 'image' in request.FILES:
                image = request.FILES['image']
                if image.content_type.startswith('image/'):
                    try:
                        upload_result = upload(image)
                        post = form.save(commit=False)
                        post.image_url = upload_result['url']
                    except Exception as e:
                        messages.error(request, 'Error uploading image: {}'.format(e))
                        return render(request, 'blog/add_post.html', {'form': form})
                else:
                    messages.error(request, 'Please upload an image file.')
                    return render(request, 'blog/add_post.html', {'form': form})
            else:
                post = form.save(commit=False)
            post.save()
            messages.success(request, 'Post added successfully!')
            return redirect('post_list')
    else:
        form = PhotoForm()
    return render(request, 'blog/add_post.html', {'form': form})

@login_required
def photo_list(request):
    """
    A view to display a list of posts.

    Returns:
    A render of the post list template with a list of posts.
    """
    posts = Post.objects.all()
    return render(request, 'blog/photo_list.html', {'post_list': post_list})

@login_required
def create_photo(request):
    """
    Create a new photo.

    Returns:
    A redirect to the blog view if the form is valid, otherwise a render of the create post template.
    """
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
def photo_detail(request):
    photo = Photo.objects.get(pk=pk)
    return reder(request, 'blog/photo_detail.html', {'photo': photo})

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
    photo = Photo.object.get(pk=pk)
    photo.delete()
    return redirect('photo_list')

def post_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo_list.html', {'photos': photos})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')

def blog_view(request):
    photos = Photo.objects.all()
    return render(request, 'blog.html', {'photos': photos})

class PhotoListView(ListView):
    model = Photo
    template_name = 'blog.html'

class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photo_detail.html'

def category_view(request, category):
    category_photos = Photo.objects.filter(category__name=category)
    return render(request, 'category.html', {'category': category, 'photos': category_photos})

def upload_landscape_image(request):
    if request.method == 'POST':
        form = LandscapeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('photo_list')
    else:
        form = LandscapeImageForm()
    return render(request, 'upload_landscape_image.html', {'form': form})

def portrait_image_list(request):
    portrait_images = Photo.objects.filter(category__name='Portrait')
    return render(request, 'portrait_image_list.html', {'images': portrait_images})

def upload_portrait_image(request):
    if request.method == 'POST':
        form = PortraitImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image uploaded successfully!')
            return redirect('portrait_image_list')
    else:
        form = PortraitImageForm()
    return render(request, 'upload_portrait_image.html', {'form': form})

def wildlife_image_list(request):
    wildlife_images = Photo.objects.filter(category__name='Wildlife')
    return render(request, 'wildlife.html', {'images': wildlife_images})

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