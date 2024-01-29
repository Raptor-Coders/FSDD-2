from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    startDate = serializers.DateField(source='start_date')
    endDate = serializers.DateField(source='end_date')
    sessionDuration = serializers.IntegerField(source='session_duration')
    isFeatured = serializers.BooleanField(source='is_featured')
    imageUrl = serializers.CharField(source='image_url')

    tags = serializers.SerializerMethodField(source='tags')

    def get_tags(self, obj):
        return obj.tags.split(',')

    class Meta:
        model = Course
        # fields = '__all__'
        fields = ['id', 'name', 'description', 'sessions', 'sessionDuration', 'startDate', 'endDate', 'tags', 'isFeatured', 'imageUrl']
