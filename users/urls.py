from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('edit/<int:pk>/', user_views.edit_user, name='edit_user'),
]
