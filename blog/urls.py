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
    path('photos/', views.PhotoListView.as_view(), name='photo_list'),
    path('category/<str:category>/', category_view, name='category'),
    path('upload_landscape_image/', views.upload_landscape_image, name='upload_landscape_image'),
    path('upload_portrait_image/', views.upload_portrait_image, name='upload_portrait_image'),
    path('portrait_image_list/', views.portrait_image_list, name='portrait_image_list'),
    path('upload_wildlife_image/', views.upload_wildlife_image, name='upload_wildlife_image'),
    path('wildlife_image_list/', views.wildlife_image_list, name='wildlife_image_list'),
    path('upload_street_image/', views.upload_street_image, name='upload_street_image'),
    path('street_image_list/', views.street_image_list, name='street_image_list'),
    path('upload_macro_image/', views.upload_macro_image, name='upload_macro_image'),
    path('macro_image_list/', views.macro_image_list, name='macro_image_list'),
    path('add_post/', views.add_photo, name='add_photo'),
    path('posts/', views.post_list, name='post_list'),
]

handler400 = 'blog.views.handler400'
handler403 = 'blog.views.handler403'
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'