from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import post_list, blog_post_detail

urlpatterns = [
    path('', post_list, name='homepage'),
    path('account/signout/', LogoutView.as_view(next_page='homepage'), name='account_signout'),
    path('blog/', blog_post_detail, name='blog_post_detail'),
]