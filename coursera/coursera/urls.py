"""
URL configuration for coursera project.

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
from django.urls import path, include
from courses.views import index
from countries.views import country
# from students.views import students
from email_subscriptions.views import subscription
from contacts.views import contact
from courses import views as courses_views
# from students import views as students_views
# from contacts import views as contacts_views
# from email_subscriptions import views as subscriptions_views

urlpatterns = [
    path('country/', country),
    path('admin/', admin.site.urls),
    path('api/students/', include('students.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/subscriptions/', include('email_subscriptions.urls')),
    path('api/contacts/', include('contacts.urls')),
    path('courses/', include('courses.urls')),
    path('contact/', include('contacts.urls')),
    path('subscriptions/', include('email_subscriptions.urls')),

    # path('contact/', include('contacts.urls')),
    # path('', index),
    # path('', courses_views.index, name='index'),
    # path('course_list', courses_views.course_list, name='course_list'),
    # path('contact/', contact),
    # path('subscriptions/', subscription),
    # path('students/', students),
    # path('courses/', courses_views.CourseListCreateView.as_view(), name='courses-list-create'),
    # path('courses/<int:pk>/', courses_views.CourseRetrieveUpdateDeleteView.as_view(), name='courses-retrieve-update-delete'),
    # path('api/students/', students_views.StudentCreate.as_view(), name='students-list-create'),
    # path('api/students/<int:pk>/', students_views.StudentDetails.as_view(), name='students-retrieve-update-delete'),
    # path('subscriptions/', subscriptions_views.EmailSubscriptionListCreateView.as_view(), name='subscription-list-create'),
    # path('subscriptions/<int:pk>/', subscriptions_views.EmailSubscriptionRetrieveUpdateDeleteView.as_view(), name='subscription-retrieve-update-delete'),
     # path('contacts/', contacts_views.ContactListCreateView.as_view(), name='contacts-list-create'),
    # path('contacts/<int:pk>/', contacts_views.ContactRetrieveUpdateDeleteView.as_view(), name='contacts-retrieve-update-delete'),
]
