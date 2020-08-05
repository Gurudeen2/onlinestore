from django.db import models
from datetime import datetime

class Cart(models.Model):
    name = models.CharField(max_length=200)
    idd = models.IntegerField()
    username = models.CharField(max_length=200)
    cart_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
