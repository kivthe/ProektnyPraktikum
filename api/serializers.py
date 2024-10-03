from rest_framework import serializers
from .models import Car, Image

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = ('id','name','picture_code','manufacturer','shipper','price','price_currency','created_at')

class CreateCarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = ('name','manufacturer','shipper','price','price_currency')

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = ('image_code','image_path')