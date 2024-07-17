from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.views import LogoutView, LoginView
from blog.models import Image, Post, Photo, Category
from.forms import LandscapeImageForm, PostForm
from cloudinary.uploader import upload

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

def signup_view(request):
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
def homepage_view(request):
    """
    A view to display the homepage.

    Returns:
    A render of the homepage template.
    """
    return render(request, 'blog/homepage.html')

def about(request):
    """
    A view to display the about page.

    Returns:
    A render of the about template.
    """
    return render(request, 'blog/about.html')

def blog_view(request):
    """
    A view to display the blog page.

    Returns:
    A render of the blog template.
    """
    return render(request, 'blog/blog.html')

def signup_view(request):
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

def category_view(request, category: str):
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

@login_required
def upload_landscape_image(request):
    """
    A view to handle landscape image upload.

    Returns:
    A render of the upload landscape image template with a form, or a redirect to the landscape image list if the form is valid.
    """
    if request.method == 'POST':
        form = LandscapeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.category = 'Landscape'
            image.save()
            return redirect('landscape')
    else:
        form = ImageForm()
    return render(request, 'blog/landscape.html', {'form': form, 'images': Image.object.filter(category='Landscape')})


@login_required
def upload_portrait_image(request):
    """
    A view to handle portrait image upload.

    Returns:
    A render of the upload portrait image template with a form, or a redirect to the portrait image list if the form is valid.
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.category = 'Portrait'
            image.save()
            return redirect('portrait')
    else:
        form = ImageForm()
    return render(request, 'blog/portrait.html', {'form': form, 'images': Image.object.filter(category='Portrait')})

@login_required
def upload_wildlife_image(request):
    """
    A view to handle wildlife image upload.

    Returns:
    A render of the upload wildlife image template with a form, or a redirect to the wildlife image list if the form is valid.
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.category = 'Wildlife'
            image.save()
            return redirect('wildlife_image_list')
    else:
        form = ImageForm()
    return render(request, 'blog/wildlife.html', {'form': form, 'images': Image.objects.filter(category='Wildlife')})

@login_required
def upload_street_image(request):
    """
    A view to handle street image upload.

    Returns:
    A render of the upload street image template with a form, or a redirect to the street image list if the form is valid.
    """
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.category = 'Street'
            image.save()
            return redirect('street')
    else:
        form = ImageForm()
    return render(request, 'blog/street.html', {'form': form, 'images': Image.object.filter(category='Street')})

@login_required
def upload_macro_image(request):
    if request.method == 'POST':
        """
    A view to handle macro image upload.

    Returns:
    A render of the upload macro image template with a form, or a redirect to the macro image list if the form is valid.
    """
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.category = 'Macro'
            image.save()
            return redirect('macro')
    else:
        form = ImageForm()
    return render(request, 'blog/macro.html', {'form': form, 'images': Image.object.filter(category='Macro')})

@login_required
def add_post(request):
    """
    A view to handle post creation.

    Returns:
    A render of the add post template with a form, or a redirect to the post list if the form is valid.
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
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
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})


def post_list(request):
    """
    A view to display a list of posts.

    Returns:
    A render of the post list template with a list of posts.
    """
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def create_post(request):
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

@login_required
def landscape_image_list(request):
    """
    A view to display a list of landscape images.

    Returns:
    A render of the landscape image list template with a list of landscape images.
    """
    images = Image.objects.filter(category='Landscape')
    return render(request, 'landscape_image_list.html', {'images': images})

@login_required
def portrait_image_list(request):
    """
    A view to display a list of portrait images.

    Returns:
    A render of the portrait image list template with a list of portrait images.
    """
    images = Image.objects.filter(category='Portrait')
    return render(request, 'portrait_image_list.html', {'images': images})

@login_required
def wildlife_image_list(request):
    """
    A view to display a list of wildlife images.

    Returns:
    A render of the wildlife image list template with a list of wildlife images.
    """
    images = Image.objects.filter(category='Wildlife')
    return render(request, 'wildlife_image_list.html', {'images': images})

@login_required
def street_image_list(request):
    """
    A view to display a list of street images.

    Returns:
    A render of the street image list template with a list of street images.
    """
    images = Image.objects.filter(category='Street')
    return render(request, 'street_image_list.html', {'images': images})

@login_required
def macro_image_list(request):
    """
    A view to display a list of macro images.

    Returns:
    A render of the macro image list template with a list of macro images.
    """
    images = Image.objects.filter(category='Macro')
    return render(request, 'macro_image_list.html', {'images': images})

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