from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=240)
    descript = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    path = models.ImageField(upload_to="imagens/")

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now, blank=True)
    members = models.ManyToManyField(
        Product,
        through="CartItem",
        through_fields=("cart", "product"),
    )

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()