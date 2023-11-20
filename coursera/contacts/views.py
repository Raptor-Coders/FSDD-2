from django.forms.models import BaseModelForm
from rest_framework import generics
from .models import Contact
from .forms import ContactForm
from .serializers import ContactSerializer
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib import messages




class ContactCreate(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # Basic Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# class ContactListCreateView(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer

class ContactDetails(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # Basic Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# class ContactRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer

def contact(request):
    return HttpResponse('This is the Contact page')

# class contact():
#     pass

class ContactFormView(CreateView):
    model = Contact
    # fields = [
    #     'fullname',
    #     'email',
    # ]

    form_class = ContactForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )

        return super().form_valid(form)
    
    # template_name = 'contacts_form.html'
