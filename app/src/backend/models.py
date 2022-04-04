from django.db import models

# Create your models here.

class Medterm(models.Model):
    term = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    japanese = models.CharField(max_length=50)
    def __str__(self):
        return self.term
