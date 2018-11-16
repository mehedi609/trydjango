from django.db import models
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, default='test@gmail.edu')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    summary = models.TextField(default=False)

    def get_absolute_url(self):
        # return reverse('products:dynamic_view', kwargs={'my_id': self.id})
        return reverse('products:dynamic_view', args=[self.pk])

    def __str__(self):
        return self.title
