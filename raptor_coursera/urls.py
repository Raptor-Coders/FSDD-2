"""
URL configuration for raptor_coursera project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from courses import views as courses_views
from contacts import views as contacts_views
from students import views as students_views
from email_subscriptions import views as emailsubscriptions_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/courses/', courses_views.CourseCreateView.as_view(), name='courses-create'),
    path('api/v1/courses/<int:pk>/', courses_views.CourseRetrieveUpdateDeleteView.as_view(), name='courses-retrieve-update-delete'),
    path('contacts/', contacts_views.ContactCreateView.as_view(), name='contacts-create'),
    path('contacts/<int:pk>/', contacts_views.ContactRetrieveView.as_view(), name='contacts-retrieve'),
    path('api/v1/students/', students_views.StudentCreateView.as_view(), name='students-create'),
    path('api/v1/students/<int:pk>/', students_views.StudentRetrieve.as_view(), name='students-retrieve'),
    path('emailsubscriptions/', emailsubscriptions_views.EmailSubscriptionCreateView.as_view(), name='emailsubscriptions-create'),
    path('emailsubscriptions/<int:pk>/', emailsubscriptions_views.EmailSubscriptionRetrieveView.as_view(), name='emailsubscriptions-retrieve'),
 ]