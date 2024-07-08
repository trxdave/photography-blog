from django.shortcuts import render
from .models import Category

def add_post(request):
    categories = Category.objects.all()
    return render(request, 'add_post.html', {'categories': categories})