from django import forms
from .models import EmailSubscription

class EmailSubscriptionForm(forms.ModelForm):
    class Meta:
        model = EmailSubscription
        fields = ('email', 'isSubscribed')

        widgets ={
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            # 'isSubscribed': forms.BooleanField(attrs={'class': 'form-control'})
        }