from django.urls import path
from . import views
from . views import contact

urlpatterns = [
    path('', views.ContactCreate.as_view(), name='contacts-create'),
    path('<int:pk>/', views.ContactDetails.as_view(), name='contacts-retrieve'),
    path('contact_us/', views.ContactFormView.as_view(), name='contact-us'),
]
