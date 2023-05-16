from django.db import models


# Create your models here.

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title

