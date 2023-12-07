# Generated by Django 3.2.5 on 2023-10-06 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_rename_image_data_datascrapimages_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datascrapimages',
            name='img',
        ),
        migrations.AddField(
            model_name='datascrapimages',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]