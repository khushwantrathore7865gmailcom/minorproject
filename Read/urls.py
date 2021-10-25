from django.urls import include, path, reverse_lazy
from .views import SignUpView, Login, Home, Index
from . import views
from django.contrib.auth import views as auth_views  # import this

app_name = 'Read'
urlpatterns = [
    path('home/', Home, name='home'),
    path('login', views.Login, name='Read/login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('signup', SignUpView.as_view(), name='Read/register'),
    path('', Index, name='index')
]
