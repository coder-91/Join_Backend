from rest_framework import viewsets, filters
from rest_framework.views import APIView

from authentication.models import UserProfile
from authentication.serializers import UserProfileSerializer
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from authentication import permissions


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserProfileSerializer
    authentication_classes = (BasicAuthentication, TokenAuthentication,)
    # permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class RegisterView(APIView):
    def post(self, request):
        pass


class LoginView(APIView):
    def post(self, request):
        pass


class LogoutView(APIView):
    def post(self, request):
        pass
