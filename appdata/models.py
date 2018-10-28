from django.db import models
from django.urls import reverse
# Create your models here.
class data(models.Model):
    info=models.TextField()

    def get_absolute_url(self):
        return reverse('data-list')