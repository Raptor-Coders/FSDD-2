# Generated by Django 4.2.6 on 2023-10-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='query',
        ),
        migrations.AddField(
            model_name='student',
            name='fullname',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]
