# Generated by Django 5.1 on 2024-08-17 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('About', '0002_alter_certifications_certificate_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certifications',
            name='certificate_image',
        ),
        migrations.RemoveField(
            model_name='certifications',
            name='cover_image',
        ),
        migrations.AddField(
            model_name='certifications',
            name='certificate_image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='certifications',
            name='cover_image_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
