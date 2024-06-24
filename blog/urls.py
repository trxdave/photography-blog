from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import PhotoListView, PhotoDetailView, signup_view, homepage_view, about
from . import views

urlpatterns = [
    path('photo/', views.PhotoListView.as_view(), name='photo_list'),
    path('photo/<pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signout/', views.SignoutView.as_view(), name='signout'),
    path('signup/', views.signup_view, name='signup'),
    path('homepage/', views.homepage_view, name='homepage'),
    path('blog/', views.blog_view, name='blog'),
    path('about/', views.about, name='about'),
]