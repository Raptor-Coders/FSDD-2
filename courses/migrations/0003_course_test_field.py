# Generated by Django 4.2.5 on 2023-10-02 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_max_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='test_field',
            field=models.TextField(blank=True),
        ),
    ]
