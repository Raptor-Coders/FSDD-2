from django.urls import path
from . import views

urlpatterns =[
    path('', views.EmailSubscriptionCreate.as_view(), name='subscription-create' ),
    path('<int:pk>/', views.EmailSubscriptionDetails.as_view(), name='subscription-retrieve' ),
    path('new_subscription/', views.EmailSubscriptionFormView.as_view(), name='new-subscription' ),
]
