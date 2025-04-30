"""Views for the user API."""
from django.contrib.auth import logout
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.settings import api_settings
from rest_framework import filters, status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView

from user import permissions
from user.models import User
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer, GuestSerializer,
)


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserViewSet(viewsets.ModelViewSet):
    """List all users."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class CreateGuestView(generics.CreateAPIView):
    """Create a new guest."""
    serializer_class = GuestSerializer
    token = ''

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        user.date_joined = timezone.now()
        user.save()
        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data

        return Response({
            'token': token.key,
            'user': user_data
        }, status=status.HTTP_201_CREATED)


class GuestLogoutView(APIView):
    """Logout a guest and delete."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if request.user.is_guest:
            request.user.auth_token.delete()
            request.user.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        user_data = UserSerializer(user).data
        return Response({
            'token': token.key,
            'user': user_data
        }, status=status.HTTP_200_OK)


class LogoutView(APIView):
    """Logout the authenticated user."""
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
