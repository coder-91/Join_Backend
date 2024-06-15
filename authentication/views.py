from rest_framework import viewsets
from authentication.models import UserProfile
from authentication.serializers import UserProfileSerializer


# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('id')
    serializer_class = UserProfileSerializer
    permission_classes = []