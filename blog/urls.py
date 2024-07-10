from django.urls import path
from. import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from.views import PhotoListView, PhotoDetailView, signup_view, homepage_view, about, blog_view, category_view

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('login/', auth_views.LoginView.as_view(), name='signin'),
    path('signup/', signup_view, name='signup'),
    path('signout/', LogoutView.as_view(next_page='signout.html'), name='signout'),
    path('about/', about, name='about'),
    path('blog/', blog_view, name='blog'),
    path('photo/<pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('photos/', PhotoListView.as_view(), name='photo_list'),
    path('category/<str:category>/', category_view, name='category'),
    path('upload_landscape_image/', views.upload_landscape_image, name='upload_landscape_image'),
    path('landscape_image_list/', views.landscape_image_list, name='landscape_image_list'),
    path('add_post/', views.add_post, name='add_post'),
    path('posts/', views.post_list, name='post_list'),
]