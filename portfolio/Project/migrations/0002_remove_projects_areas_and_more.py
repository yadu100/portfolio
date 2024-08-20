# Generated by Django 5.1 on 2024-08-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='areas',
        ),
        migrations.RemoveField(
            model_name='projects',
            name='project_cover_url',
        ),
        migrations.AddField(
            model_name='projects',
            name='area1',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='area2',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='area3',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='area4',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
