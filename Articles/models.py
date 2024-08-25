from django.db import models
import uuid

# Create your models here.
class Articles(models.Model):
    entry_num = models.IntegerField(null=True, blank=True)
    heading = models.CharField(max_length=800, null=True, blank=True)
    key_point = models.CharField(max_length=200, null=True, blank=True)

    date = models.DateField(null=True, blank=True, auto_now_add=True)

    minute_read = models.CharField(max_length=5, null=True, blank=True)

    primary_note = models.CharField(max_length=1000, null=True, blank=True)

    sub_heading1 = models.CharField(max_length=800, null=True, blank=True)
    picture1 = models.CharField(max_length=500, null=True, blank=True)
    sub_text1 = models.TextField(max_length=1200, null=True, blank=True)

    sub_heading2 = models.CharField(max_length=800, null=True, blank=True)
    picture2 = models.CharField(max_length=500, null=True, blank=True)
    sub_text2 = models.TextField(max_length=1200, null=True, blank=True)

    sub_heading3 = models.CharField(max_length=800, null=True, blank=True)
    picture3 = models.CharField(max_length=500, null=True, blank=True)
    sub_text3 = models.TextField(max_length=1200, null=True, blank=True)

    sub_heading4 = models.CharField(max_length=800, null=True, blank=True)
    picture4 = models.CharField(max_length=500, null=True, blank=True)
    sub_text4 = models.TextField(max_length=1200, null=True, blank=True)

    sub_heading5 = models.CharField(max_length=800, null=True, blank=True)
    picture5 = models.CharField(max_length=500, null=True, blank=True)
    sub_text5 = models.TextField(max_length=1200, null=True, blank=True)


    conclusion = models.TextField(max_length=1200, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)


    def __str__(self) -> str:
        return self.heading

