# Generated by Django 5.1 on 2024-08-20 09:35

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('entry_num', models.IntegerField(blank=True, null=True)),
                ('project_name', models.CharField(blank=True, max_length=500, null=True)),
                ('project_type', models.CharField(blank=True, max_length=200, null=True)),
                ('project_cover_url', models.CharField(blank=True, max_length=800, null=True)),
                ('project_homepage_url', models.CharField(blank=True, max_length=800, null=True)),
                ('areas', models.TextField(blank=True, max_length=2000, null=True)),
                ('short_description', models.CharField(blank=True, max_length=800, null=True)),
                ('long_description', models.TextField(blank=True, max_length=2000, null=True)),
                ('techs_used', models.TextField(blank=True, max_length=2000, null=True)),
                ('status', models.CharField(blank=True, choices=[('Completed', 'Completed'), ('On Going', 'On Going')], max_length=200, null=True)),
                ('project_url', models.CharField(blank=True, max_length=500, null=True)),
                ('source_code_url', models.CharField(blank=True, max_length=500, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
