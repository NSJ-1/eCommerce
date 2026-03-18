from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    """
    Represents a product in the eCommerce app.
    
    Each product has a name, price and belongs to a user who owns the product.
    """

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return the name of the product to its string representation.
        """
        return self.name

class Store(models.Model):
    """
    Represents a store created by a vendor.

    A store contains products and is associated with vendor (user).
    """

    vendor = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        """
        Return the name of the store to its string representation.
        """
        return self.name
