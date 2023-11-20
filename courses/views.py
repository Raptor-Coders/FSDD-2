from django.shortcuts import render
from rest_framework import generics
from courses.models import Course
from .serializers import CourseSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class CourseCreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Basic Athentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class CourseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Basic Athentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]