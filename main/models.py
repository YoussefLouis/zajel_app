from django.db import models

class DimHub(models.Model):
    hub_id = models.AutoField(primary_key=True)
    shortcode = models.CharField(max_length=10)
    name_en = models.CharField(max_length=255)
    name_ar = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    governorate_id = models.IntegerField()
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name_en

