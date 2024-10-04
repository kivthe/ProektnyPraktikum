from rest_framework import serializers
from .models import Car, Image, Page, CarlosonCar, RentrideCar, React

#====================================================================================================

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = ('id','name','picture_code','manufacturer','shipper','price','price_currency','created_at')

#====================================================================================================

class CreateCarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = ('name','manufacturer','shipper','price','price_currency')

#====================================================================================================

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = ('image_code','image_path')

#====================================================================================================

class PageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Page
    fields = ('page_code','page_index_path')

#====================================================================================================

class CarlosonCarSerializer(serializers.ModelSerializer):
  class Meta:
    model = CarlosonCar
    fields = ('link','engine_volume','power','year','fuel_type','drive_type','img')

#====================================================================================================

class RentrideCarSerializer(serializers.ModelSerializer):
  class Meta:
    model = RentrideCar
    fields = ('link','engine','drive','year')

#====================================================================================================

class ReactSerializer(serializers.ModelSerializer):
  class Meta:
    model = React
    fields = ('name','detail')

#====================================================================================================