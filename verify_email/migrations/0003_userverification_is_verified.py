# Generated by Django 4.2.7 on 2023-11-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verify_email', '0002_userverification'),
    ]

    operations = [
        migrations.AddField(
            model_name='userverification',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
