from django.db import models
import uuid
# Create your models here.


#Creating Certifications table for about page

class Certifications(models.Model):
    cover_image_url = models.CharField(max_length=500, null=True, blank=True)
    certification_name = models.CharField(max_length=700)
    certification_description = models.TextField(max_length=1000)
    certificate_image_url =  models.CharField(max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.certification_name
