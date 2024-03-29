# Generated by Django 4.2.5 on 2023-10-15 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_name'),
        ('students', '0005_alter_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='course', to='courses.course'),
        ),
    ]
