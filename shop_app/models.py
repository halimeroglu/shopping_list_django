from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.CharField(max_length = 150,blank=True,null=True)

    def __str__(self):
        return self.name