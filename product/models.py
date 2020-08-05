from django.db import models
from datetime import datetime
from category.models import cate
class Product(models.Model):
    category = models.ForeignKey(cate, on_delete=models.DO_NOTHING)
    prod_name = models.CharField(max_length=70, verbose_name='Product Name')
    description = models.TextField(blank=False)
    price = models.CharField(max_length=50)
    main_img = models.ImageField(upload_to='photos/%Y/%m/%d/')
    img_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    img_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    prod_date = models.DateTimeField(default=datetime.now, blank=True)
    sticky = models.BooleanField(default=False)
    def __str__(self):
        return self.prod_name
