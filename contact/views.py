from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication


from contact.models import Contact
from contact.serializers import ContactSerializer


# Create your views here.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer
    #authentication_classes = (TokenAuthentication,)
    permission_classes = []