# Generated by Django 4.2.6 on 2023-10-09 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_session_course_sessions'),
        ('students', '0002_remove_student_query_student_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='courses.course'),
        ),
    ]
