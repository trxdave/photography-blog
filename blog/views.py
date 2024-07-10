from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.views.generic import ListView, DetailView
from .models import Category, Post, Photo, LandscapeImage
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LandscapeImageForm, PostForm

class PhotoListView(ListView):
    """
    A view to display a list of photos.

    Attributes:
    model: The model to use for the view.
    template_name: The template to use for the view.
    context_object_name: The name to use for the object list in the template.
    """
    model = Photo
    template_name = 'blog.html'
    context_object_name = 'post_list'

class PhotoDetailView(DetailView):
    """
    A view to display a detailed photo.

    Attributes:
    model: The model to use for the view.
    template_name: The template to use for the view.
    """
    model = Photo
    template_name = 'blog/photo_detail.html'

class SignoutView(LogoutView):
    """
    A view to handle user signout.

    Attributes:
    template_name: The template to use for the view.
    next_page: The URL to redirect to after signout.
    """
    template_name = 'account/logout.html'
    next_page = '/'

class SigninView(LoginView):
    """
    A view to handle user signin.

    Attributes:
    template_name: The template to use for the view.
    """
    template_name = 'blog/signin.html'

def signup_view(request) -> render:
    """
    A view to handle user signup.

    Returns:
    A render of the signup template with a form, or a redirect to the blog view if the form is valid.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_view')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

@login_required
def homepage_view(request) -> render:
    """
    A view to display the homepage.

    Returns:
    A render of the homepage template.
    """
    return render(request, 'blog/homepage.html')

def about(request) -> render:
    """
    A view to display the about page.

    Returns:
    A render of the about template.
    """
    return render(request, 'blog/about.html')

def blog_view(request) -> render:
    """
    A view to display the blog page.

    Returns:
    A render of the blog template.
    """
    return render(request, 'blog/blog.html')

def signup_view(request) -> render:
    """
    A view to handle user signup.

    Returns:
    A render of the signup template with a form, or a redirect to the blog view if the form is valid.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog_view')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def category_view(request, category: str) -> render:
    """
    A view to display photos by category.

    request: The HTTP request object.
    category: The category to filter by.

    Returns:
    A render of the category template with a list of photos, or a 404 error if the category does not exist.
    """
    category_obj = Category.objects.filter(name=category).first()
    if category_obj:
        photos = Photo.objects.filter(category=category_obj)
        return render(request, 'blog/category.html', {'photos': photos, 'category': category})
    else:
        return render(request, 'errors/404.html')

def upload_landscape_image(request) -> render:
    """
    A view to handle landscape image upload.

    Returns:
    A render of the upload landscape image template with a form, or a redirect to the landscape image list if the form is valid.
    """
    if request.method == 'POST':
        form = LandscapeImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landscape_image_list')
    else:
        form = LandscapeImageForm()
    return render(request, 'upload_landscape_image.html', {'form': form})

@login_required
def add_post(request) -> render:
    """
    A view to handle post creation.

    Returns:
    A render of the add post template with a form, or a redirect to the post list if the form is valid.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def post_list(request) -> render:
    """
    A view to display a list of posts.

    Returns:
    A render of the post list template with a list of posts.
    """
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def create_post(request) -> redirect:
    """
    Create a new post.

    Returns:
    A redirect to the blog view if the form is valid, otherwise a render of the create post template.
    """
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

def landscape_image_list(request) -> render:
    """
    A view to display a list of landscape images.

    Returns:
    A render of the landscape image list template with a list of landscape images.
    """
    images = LandscapeImage.objects.all()
    return render(request, 'landscape_image_list.html', {'images': images})

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