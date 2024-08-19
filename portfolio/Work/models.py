from django.db import models
import uuid
# Create your models here.

class Experiences(models.Model):
    entry_num = models.IntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=200, null=True, blank=True)
    company_image_url = models.CharField(max_length=700, null=True, blank=True)
    designation = models.CharField(max_length=200, null=True, blank=True)
    department = models.CharField(max_length=200, null=True, blank=True)
    start_year = models.CharField(max_length=5, null=True, blank=True)
    end_year = models.CharField(max_length=10, null=True, blank=True)
    total_years = models.CharField(max_length=5, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    short_description = models.CharField(max_length=800, null=True, blank=True)
    long_description  = models.TextField(max_length=1500, null=True, blank=True)
    techs_used = models.CharField(max_length=800, null=True, blank=True)
    duty1 = models.CharField(max_length=800, null=True, blank=True)
    duty2 = models.CharField(max_length=800, null=True, blank=True)
    duty3 = models.CharField(max_length=800, null=True, blank=True)
    duty4 = models.CharField(max_length=800, null=True, blank=True)
    company_url = models.CharField(max_length=700, null=True, blank=True)
    company_linkedin = models.CharField(max_length=700, null=True, blank=True)



    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.company_name
