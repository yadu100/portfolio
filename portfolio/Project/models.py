from django.db import models
import uuid
# Create your models here.


class Projects(models.Model):
    entry_num = models.IntegerField(null=True, blank=True)
    project_name = models.CharField(max_length=500, null=True, blank=True)
    project_type = models.CharField(max_length=200, null=True, blank=True)
    
    project_homepage_url = models.CharField(max_length=800, null=True,blank=True)

    area1 = models.CharField(max_length=800, null=True,blank=True)
    area2 = models.CharField(max_length=800, null=True,blank=True)
    area3 = models.CharField(max_length=800, null=True,blank=True)
    area4 = models.CharField(max_length=800, null=True,blank=True)

    short_description = models.CharField(max_length=800, null=True,blank=True)
    long_description = models.TextField(max_length=2000, null=True, blank=True)

    techs_used = models.TextField(max_length=2000, null=True,blank=True)


    status_choices = (('Completed','Completed'),
                      ('On Going','On Going')
                      )

    status = models.CharField(max_length=200, null=True, blank=True, choices=status_choices)

    project_url = models.CharField(max_length=500, null=True,blank=True)
    source_code_url = models.CharField(max_length=500, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self) -> str:
        return self.project_name
    
