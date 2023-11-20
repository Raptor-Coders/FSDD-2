from email_subscriptions.models import EmailSubscription

def emailSubscription_emailSender_newCourse():
    EmailSubscription.create_instance('Your email subscription has been confirmed')


