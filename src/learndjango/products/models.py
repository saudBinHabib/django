from django.db import models


# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    summary = models.TextField(default="this product is cool!")

    def absolute_url(self):
        return f'/product/{self.id}'
