# Generated by Django 4.2.5 on 2023-10-02 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='max_students',
            field=models.IntegerField(default=3),
        ),
    ]