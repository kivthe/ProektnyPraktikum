from django.db import models

#====================================================================================================

class Car(models.Model):
  name = models.CharField(max_length=128,null=False,default="")
  picture_code = models.CharField(max_length=32,default="")
  manufacturer = models.CharField(max_length=128,default="") 
  shipper = models.CharField(max_length=128,default="")
  price = models.IntegerField(null=False,default=0)
  price_currency = models.CharField(max_length=32,null=False,default="USD")
  created_at = models.DateTimeField(auto_now_add=True)

#====================================================================================================

class Image(models.Model):
  image_code = models.IntegerField(primary_key=True,default=0)
  image_path = models.CharField(max_length=256,null=False,default="")

#====================================================================================================

class Page(models.Model):
  page_code = models.IntegerField(primary_key=True,default=0)
  page_index_path = models.CharField(max_length=256,null=False,default="index.html")

#====================================================================================================

class CarlosonCar(models.Model):
  link = models.CharField(max_length=512,primary_key=True,default="Unknown")
  engine_volume = models.CharField(max_length=128,default="Unknown")
  power = models.CharField(max_length=32,default="Unknown")
  year = models.CharField(max_length=8,default="Unknown")
  fuel_type = models.CharField(max_length=32,default="Unknown")
  drive_type = models.CharField(max_length=32,default="Unknown")
  img = models.CharField(max_length=1024,default="Unknown") 

#====================================================================================================

class RentrideCar(models.Model):
  link = models.CharField(max_length=512,primary_key=True,default="Unknown")
  engine = models.CharField(max_length=128,default="Unknown")
  drive = models.CharField(max_length=32,default="Unknown")
  year = models.CharField(max_length=8,default="Unknown")
  #img = models.CharField(max_length=1024,default="Unknown") 

#====================================================================================================