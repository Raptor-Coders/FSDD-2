from rest_framework import serializers
from email_subscriptions.models import EmailSubscription

class EmailSubscriptionSerializer (serializers.ModelSerializer):

    class Meta: 
        model = EmailSubscription
        fields = '__all__'
