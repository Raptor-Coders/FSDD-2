from typing import Any
from django.db import models
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.views.generic import ListView, DetailView


class CourseCreate(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Basic Authentication
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

# class CourseListCreateView(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

class CourseDetails(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# class CourseRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# Copy items from old computer here!

# from django.shortcuts import render

# # Create your views here.
def index(request):
    # print('Im in the index function')
    # return
    # return HttpResponse("Welcome to Course app")
    return render(request, 'courses/base.html')


# def course_list(request):
#     courses = Course.objects.all()
#     context = {'course_list': courses}
#     return render(request, 'courses/course_list.html', context)

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset
