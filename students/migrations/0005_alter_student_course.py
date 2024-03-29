# Generated by Django 4.2.5 on 2023-10-11 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_name'),
        ('students', '0004_rename_course_id_student_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='courses.course'),
        ),
    ]
