from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Item(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Coupon(models.Model):
    user = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    coupon_id = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)
