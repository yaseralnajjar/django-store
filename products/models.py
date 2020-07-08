from django.db import models

# Create your models here.


class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
