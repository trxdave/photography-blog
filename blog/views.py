from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from blog.models import Photo, Category, Comment
from .forms import PhotoForm, ContactForm, SignupForm, CommentForm
from django.core.paginator import Paginator
from django.db.models import Q
import cloudinary.uploader as uploader

def homepage_view(request):
    return render(request, 'blog/homepage.html')

def blog_view(request):
    photos_list = Photo.objects.all()
    paginator = Paginator(photos_list, 6)  # Show 6 photos per page

    page_number = request.GET.get('page')
    photos = paginator.get_page(page_number)

    return render(request, 'blog/blog.html', {'photos': photos})

def viewPhoto(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'blog/photo_detail.html', {'photo': photo})

@login_required
def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user      
            photo.save()            
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
    user_photos = Photo.objects.filter(user=request.user)
    paginator = Paginator(user_photos, 12)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/photo_list.html', {'page_obj': page_obj})

@login_required
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    comments = photo.comments.all()

    paginator = Paginator(comments, 3)
    page_number = request.GET.get('page')
    comments_page_obj = paginator.get_page(page_number)

    is_liked = False
    if photo.likes.filter(id=request.user.id).exists():
        is_liked = True

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.photo = photo
            new_comment.user = request.user
            new_comment.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/photo_detail.html', {
        'photo': photo,
        'comment_form': comment_form,
        'comments_page_obj': comments_page_obj,
        'is_liked': is_liked,
        'total_likes': photo.total_likes(),
    })

@login_required
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if photo.likes.filter(id=request.user.id).exists():
        photo.likes.remove(request.user)
    else:
        photo.likes.add(request.user)
    return redirect('photo_detail', pk=pk)

@login_required
def edit_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    # Check if the current logged-in user is the owner of the photo
    if not request.user == photo.user:
        # This user does not own this photo
        messages.error(request, "Access Denied: This is not your photo")
        return redirect('blog')  # Redirect to the blog page

    # This user owns this photo - proceed with the edit
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, "Photo successfully updated!")
            return redirect('blog')  # Redirect to the blog page
        else:
            messages.error(request, "Error: Please try again.")
    else:
        form = PhotoForm(instance=photo)
    
    return render(request, 'blog/edit_photo.html', {'form': form})

@login_required
def delete_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    # Check if the current logged-in user is the owner of the photo
    if not request.user == photo.user:
        # This user does not own this photo
        messages.error(request, "Access Denied: This is not your photo")
        return redirect('blog')  # Redirect to the blog page

    # This user owns this photo - proceed with the delete
    if request.method == 'POST':
        photo.delete()
        messages.success(request, "Photo successfully deleted!")
        return redirect('blog')  # Redirect to the blog page

    return render(request, 'blog/confirm_delete.html', {'photo': photo})

@login_required
def delete_comment(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, photo_id=pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('photo_detail', pk=pk)

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = SignupForm()
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

def search_view(request):
    query = request.GET.get('q')
    results = []
    
    if query:
        results = Photo.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query)
        )
    
    return render(request, 'blog/search_results.html', {'results': results, 'query': query})

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
    macro_photos = Photo.objects.filter(categoryimage__name='5')
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
        form.save()
        return redirect('success')
    return render(request, 'blog/contact.html', {'form': form})

def about(request):
    return render(request, 'blog/about.html')

def success(request):
    return render(request, 'success.html')

# Error Handlers
def handler400(request, exception):
    return render(request, 'errors/400.html', status=404)

def handler403(request, exception):
    return render(request, 'errors/403.html', status=403)

def handler404(request, exception):
    return render(request, 'errors/404.html', status=404)

def handler500(request):
    return render(request, 'errors/500.html', status=500)