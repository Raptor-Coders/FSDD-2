from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseCreate.as_view(), name='course-create'),
    path('<int:pk>/', views.CourseDetails.as_view(), name='courses-retrieve'),
    path('index/', views.index, name='index'),
    # path('course_list/', views.course_list, name='course_list'),
    path('course_list/', views.CourseListView.as_view(), name='course-list'),
    path('course_list/<int:pk>', views.CourseDetailView.as_view(), name='course-detail'),
]
