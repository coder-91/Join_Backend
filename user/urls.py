"""URL mappings for the user API."""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user import views

router = DefaultRouter()
router.register('', views.UserViewSet)

app_name = 'user'

urlpatterns = [
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('', include(router.urls)),
]