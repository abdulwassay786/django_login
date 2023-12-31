# Generated by Django 3.2.5 on 2023-09-25 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DataScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('dep', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('hierarchy', models.CharField(blank=True, max_length=255, null=True)),
                ('validation', models.BooleanField(default=False, null=True)),
            ],
        ),
    ]
