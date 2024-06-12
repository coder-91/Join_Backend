from rest_framework import viewsets
from contact.models import Contact
from contact.serializers import ContactSerializer


# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer
    permission_classes = []
