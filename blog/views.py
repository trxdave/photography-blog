from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from .models import Photo  

def post_list(request):
    posts = Photo.objects.all()
    return render(request, 'blog/photo_list.html', {'posts': posts})

class PostListView(ListView):
    model = Photo  
    template_name = 'blog/post_list.html'

post_list = PostListView.as_view()

class PostDetailView(DetailView):
    model = Photo  
    template_name = 'blog/post_detail.html'

blog_post_detail = PostDetailView.as_view()
