# Generated by Django 4.2.5 on 2023-09-30 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="default.png", upload_to="profile_pics"),
        ),
    ]