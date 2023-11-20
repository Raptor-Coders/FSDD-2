from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentCreate.as_view(), name='student-create'),
    path('<int:pk>/', views.StudentDetails.as_view(), name='students-retrieve'),
]
