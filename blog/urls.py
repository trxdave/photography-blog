from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from .views import PhotoListView, PhotoDetailView, signup_view, homepage_view, about, blog_view

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('signup/', signup_view, name='signup'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('about/', about, name='about'),
    path('blog/', blog_view, name='blog'),
    path('photo/<pk>/', PhotoDetailView.as_view(), name='photo_detail'),
]