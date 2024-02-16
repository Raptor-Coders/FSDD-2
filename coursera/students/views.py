from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentCreate(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

class StudentDetails(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Basic Authentication
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

# class StudentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

def students(request):
    return HttpResponse("Welcome to the Students Page.")
