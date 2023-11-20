
from django.shortcuts import render
from rest_framework import generics
from contacts.models import Contact
from .serializers import ContactSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # Basic Athentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


#class ContactRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Contact.objects.all()
#    serializer_class = ContactSerializer


class ContactRetrieveView(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # Basic Athentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


