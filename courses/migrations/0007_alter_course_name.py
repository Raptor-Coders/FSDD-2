# Generated by Django 4.2.5 on 2023-10-10 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_end_date_alter_course_session_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]