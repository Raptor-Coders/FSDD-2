from rest_framework import generics
from .models import EmailSubscription
from .forms import EmailSubscriptionForm
from .serializers import EmailSubscriptionSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import CreateView
from django.contrib import messages


class EmailSubscriptionCreate(generics.CreateAPIView):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer

    # Basic Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# class EmailSubscriptionListCreateView(generics.ListCreateAPIView):
#     queryset = EmailSubscription.objects.all()
#     serializer_class = EmailSubscriptionSerializer

class EmailSubscriptionDetails(generics.RetrieveAPIView):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer

    # Basic Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class EmailSubscriptionFormView(CreateView):
    model = EmailSubscription
    form_class = EmailSubscriptionForm

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you! Your message has been sent.'
        )

        return super().form_valid(form)
    
    # template_name = 'newSubscription_form.html'


# class EmailSubscriptionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = EmailSubscription.objects.all()
#     serializer_class = EmailSubscriptionSerializer

def subscription(request):
    return HttpResponse("Email Subscriptions")
