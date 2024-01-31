# Generated by Django 4.2.5 on 2023-10-02 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_image_url_alter_course_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='session_duration',
            field=models.IntegerField(help_text='Session duration in minutes'),
        ),
        migrations.AlterField(
            model_name='course',
            name='sessions',
            field=models.IntegerField(help_text='Number of sessions'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]