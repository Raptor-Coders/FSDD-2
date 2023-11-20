from django.shortcuts import render
from rest_framework import generics
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# allows List and Create
#class StudentListCreateView(generics.ListCreateAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer


# allow Create only
class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



# Allows Get, Put, Delete, Patch
#class StudentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Student.objects.all()
#    serializer_class = StudentSerializer


# Allow only Retrieve only
class StudentRetrieve(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Basic Athentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]



