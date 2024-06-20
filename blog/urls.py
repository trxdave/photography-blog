from django.urls import path
from allauth.account.views import login
from django.contrib.auth.views import LogoutView
from.views import PhotoListView, PhotoDetailView, signup_view, homepage_view, about

urlpatterns = [
    path('', homepage_view, name='homepage'),
    path('photos/', PhotoListView.as_view(), name='photo_list'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('signout/', LogoutView.as_view(), name='signout'),
    path('signin/', login, name='signin'),
    path('signup/', signup_view, name='signup'),
    path('blog/', PhotoListView.as_view(), name='blog'),
    path('about/', about, name='about'),
]