from django.db import models

class Product (models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.IntegerField()

git config --global user.email "rana29adel@gmail.com"

kmly