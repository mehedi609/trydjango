from django.db import models
from django.urls import reverse
# Create your models here.


class CourseModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass
