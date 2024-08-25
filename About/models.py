from django.db import models
import uuid

class Certifications(models.Model):
        cover_image_url = models.CharField(max_length=500, null=True, blank=True)
        certification_name = models.CharField(max_length=700)
        certification_description = models.TextField(max_length=1000)
        certificate_image_url =  models.CharField(max_length=500, null=True, blank=True)

        created = models.DateTimeField(auto_now_add=True)
        id =  models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

        def __str__(self) -> str:
                return self.certification_name