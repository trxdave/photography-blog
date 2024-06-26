from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import PhotoListView, PhotoDetailView, signup_view, homepage_view, about
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('signin/', views.SigninView.as_view(), name='signin'),
    path('signup/', auth_views.LoginView.as_view(), name='signup'),
    path('signout/', views.SignoutView.as_view(), name='signout'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('photo/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('accounts/signup/', auth_views.LoginView.as_view(), name='signup'),
]