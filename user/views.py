"""Views for the user API."""

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.views import APIView
from rest_framework import filters
from rest_framework import generics
from user.serializers import UserSerializer


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    #permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class RegisterView(APIView):
    def post(self, request):
        pass


class LoginView(APIView):
    def post(self, request):
        pass


class LogoutView(APIView):
    def post(self, request):
        pass
