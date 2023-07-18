from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    release_date = models.DateField()
    description = models.TextField()
    image_url = models.URLField(max_length=200)
