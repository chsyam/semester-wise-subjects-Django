from random import choices
from django.db import models
# Create your models here.

class semestersModel(models.Model):
    status_choices = (
        (1,"1"),
        (2,"2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
        (7, "7"),
        (8, "8"),
    )
    subject_title = models.CharField(max_length=30)
    subject_code = models.CharField(max_length=30)
    document = models.FileField(upload_to = "uploads/")
    subject_credits = models.FloatField()
    semester = models.IntegerField(choices = status_choices,default=1)