# Generated by Django 4.2.5 on 2023-10-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='fullname',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]