from django.db import models

class Car(models.Model):
  name = models.CharField(max_length=128,null=False,default="")
  picture_code = models.CharField(max_length=32,default="")
  manufacturer = models.CharField(max_length=128,default="") 
  shipper = models.CharField(max_length=128,default="")
  price = models.IntegerField(null=False,default=0)
  price_currency = models.CharField(max_length=32,null=False,default="USD")
  created_at = models.DateTimeField(auto_now_add=True)

class Image(models.Model):
  image_code = models.IntegerField(null=False,primary_key=True,default=0)
  image_path = models.CharField(max_length=256,null=False,default="")