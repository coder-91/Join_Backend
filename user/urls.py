"""URL mappings for the user API."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register('', views.UserViewSet)

app_name = 'user'

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('login/guest/', views.CreateGuestView.as_view(), name='login_guest'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('logout/guest/', views.GuestLogoutView.as_view(), name='logout_guest'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]
