from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from email_subscriptions.models import EmailSubscription
from .serializers import EmailSubscriptionSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


#class EmailSubscriptionListCreateView(generics.ListCreateAPIView):
#    queryset = EmailSubscription.objects.all()
#    serializer_class = EmailSubscriptionSerializer

# allow create only
class EmailSubscriptionCreateView(generics.CreateAPIView):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer

class EmailSubscriptionListView(generics.ListAPIView):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer

    # Basic Athentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

#class EmailSubscriptionRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = EmailSubscription.objects.all()
#    serializer_class = EmailSubscriptionSerializer

# only allow retrieval of emailsubscription
class EmailSubscriptionRetrieveView(generics.RetrieveAPIView):
    queryset = EmailSubscription.objects.all()
    serializer_class = EmailSubscriptionSerializer

   # Basic Athentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

