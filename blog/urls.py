from django.urls import path
from. import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('login/', auth_views.LoginView.as_view(), name='signin'),
    path('signup/', views.signup_view, name='signup'),
    path('signout/', LogoutView.as_view(next_page='signout.html'), name='signout'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_view, name='blog'),
    path('photo/<pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('photos/', views.PhotoListView.as_view(), name='photo_list'),
    path('category/<slug:category_slug>/', views.category_view, name='category'),
    path('upload/', views.add_photo, name='upload'),
    path('add_photo/', views.add_photo, name='add_photo'),
    path('posts/', views.photo_list, name='post_list'),
    path('landscape/', views.landscape_photos, name='landscape_photos'),
    path('portrait/', views.portrait_photos, name='portrait_photos'),
    path('wildlife/', views.wildlife_photos, name='wildlife_photos'),
    path('street/', views.street_photos, name='street_photos'),
    path('macro/', views.macro_photos, name='macro_photos'),
]

handler400 = 'blog.views.handler400'
handler403 = 'blog.views.handler403'
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'