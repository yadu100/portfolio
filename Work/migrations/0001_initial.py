# Generated by Django 5.1 on 2024-08-18 10:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiences',
            fields=[
                ('company_name', models.CharField(blank=True, max_length=200, null=True)),
                ('company_image_url', models.CharField(blank=True, max_length=700, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('start_year', models.CharField(blank=True, max_length=5, null=True)),
                ('end_year', models.CharField(blank=True, max_length=10, null=True)),
                ('total_years', models.CharField(blank=True, max_length=5, null=True)),
                ('location', models.CharField(blank=True, max_length=50, null=True)),
                ('short_description', models.CharField(blank=True, max_length=800, null=True)),
                ('long_description', models.TextField(blank=True, max_length=1500, null=True)),
                ('techs_used', models.CharField(blank=True, max_length=800, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
