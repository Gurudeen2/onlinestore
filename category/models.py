from django.db import models

class cate (models.Model):
    cate_name = models.CharField(max_length=50)
    def __str__(self):
        return self.cate_name