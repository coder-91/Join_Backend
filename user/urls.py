"""URL mappings for the user API."""

from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from user import views


app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    #path('register/', views.RegisterView.as_view()),
    #path('login/', views.CustomUserLoginApiView.as_view()),
    #path('logout/', views.LogoutView.as_view()),
    #path('token/', obtain_auth_token, name='token'),
]