from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
from users.views import NewUser, UpdateUser, DeleteUser, UserList


urlpatterns = [
    path('signup/', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', user_views.profile, name='profile'),
    path('create/', NewUser.as_view(), name='new_user'),
    path('lista/', UserList.as_view(), name='users_list'),
    path('edit/<int:pk>/', UpdateUser.as_view(), name='edit_user'),
    path('delete/<int:pk>/', DeleteUser.as_view(), name='delete_user'),

]
