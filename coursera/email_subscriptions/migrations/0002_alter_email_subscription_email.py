# Generated by Django 4.2.5 on 2023-10-07 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_subscription',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
