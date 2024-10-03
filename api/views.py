from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
from django.template import loader
from .serializers import CarSerializer, CreateCarSerializer, ImageSerializer, PageSerializer
from .models import Car, Image, Page

#====================================================================================================

class CarView(generics.ListAPIView):
  serializer_class = CarSerializer
  def get(self,request,format=None):
    cars = Car.objects.all()
    if not cars.exists():
      return Response({"Bad request":"No cars to view"},status=status.HTTP_404_NOT_FOUND)
    data = serializers.serialize('json', Car.objects.all())
    return Response(data,status=status.HTTP_200_OK)

#====================================================================================================

class CreateCarView(APIView):
  serializer_class = CreateCarSerializer
  def post(self, request, format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      name = serializer.data.get('name')
      manufacturer = serializer.data.get('manufacturer')
      shipper = serializer.data.get('shipper')
      price = serializer.data.get('price')
      price_currency = serializer.data.get('price_currency')
      query = Car.objects.filter(name=name)
      if query.exists():
        car = query[0]
        car.manufacturer = manufacturer
        car.shipper = shipper
        car.price = price
        car.price_currency = price_currency
        car.save(update_fields=['manufacturer','shipper','price','price_currency'])
        return Response(CarSerializer(car).data,status=status.HTTP_201_CREATED)
      else:
        car = Car(manufacturer=manufacturer,shipper=shipper,price=price,price_currency=price_currency)
        car.save()
        return Response(CarSerializer(car).data,status=status.HTTP_201_CREATED)
    return Response("Serialization is invalid")

#====================================================================================================

class GetCar(APIView):
  serializer_class = CarSerializer
  lookup_url_kwarg = 'car_code'
  def get(self,request,format=None):
    code = request.GET.get(self.lookup_url_kwarg)
    if code != None:
      car = Car.objects.filter(id=code)
      if len(car) > 0:
        data = CarSerializer(car[0]).data
        return Response(data,status=status.HTTP_200_OK)
      return Response({'Bad request':'Invalid car code'},status=status.HTTP_404_NOT_FOUND)
    return Response({'Bad request':'Car code parameter not found in request'},status=status.HTTP_400_BAD_REQUEST)

#====================================================================================================

class GetImage(APIView):
  def get(self,request,format=None):
    lookup_url_kwarg = 'image_code'
    code = request.GET.get(lookup_url_kwarg)
    if code != None:
      image = Image.objects.filter(image_code=code)
      if (len(image) > 0):
        path_to_image = image[0].image_path
        img = open(path_to_image, 'rb')
        return FileResponse(img,status=status.HTTP_200_OK)
      else:
        return Response({'Bad request':'Invalid image code'},status=status.HTTP_404_NOT_FOUND)
    return Response({'Bad request':'Image code parameter not found in request'},status=status.HTTP_400_BAD_REQUEST)

#====================================================================================================

class CreateImageView(APIView):
  serializer_class = ImageSerializer
  def post(self,request,format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      img_code = serializer.data.get('image_code')
      img_path = serializer.data.get('image_path')
      query = Image.objects.filter(image_code=img_code)
      if query.exists():
        img = query[0]
        #img.image_code = img_code
        img.image_path = img_path
        img.save(update_fields=['image_path'])
        return Response(ImageSerializer(img).data,status=status.HTTP_201_CREATED)
      else:
        img = Image(image_code=img_code,image_path=img_path)
        img.save()
        return Response(ImageSerializer(img).data,status=status.HTTP_201_CREATED)
    return Response("Serialization is invalid")

#====================================================================================================

class ViewImagesView(APIView):
  serializer_class = ImageSerializer
  def get(self,request,format=None):
    images = Image.objects.all()
    if not images.exists():
      return Response({"Bad request":"No images to view"},status=status.HTTP_404_NOT_FOUND)
    data = serializers.serialize('json', Image.objects.all())
    return Response(data,status=status.HTTP_200_OK)

#====================================================================================================

class GetPage(APIView):
  lookup_url_kwarg = 'page_code'
  def get(self,request,fromat=None):
    pg_code = request.GET.get(self.lookup_url_kwarg)
    if pg_code != None:
      pg = Page.objects.filter(page_code=pg_code)
      if (len(pg) > 0):
        pg_index_path = pg[0].page_index_path
        return render(request,pg_index_path,status=status.HTTP_200_OK)
      else:
        return Response({"Bad request":"No page associated with the code page"},status=status.HTTP_404_NOT_FOUND)
    return Response({"Bad request":"No page code found in the request"})
        
#====================================================================================================

class CreatePage(APIView):
  serializer_class = PageSerializer
  def post(self,request,format=None):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
      pg_code = serializer.data.get('page_code')
      pg_index_path = serializer.data.get('page_index_path')
      query = Page.objects.filter(page_code=pg_code)
      if query.exists():
        pg = query[0]
        pg.image_path = pg_index_path
        pg.save(update_fields=['image_index_path'])
        return Response(PageSerializer(pg).data,status=status.HTTP_201_CREATED)
      else:
        pg = Page(page_code=pg_code,page_index_path=pg_index_path)
        pg.save()
        return Response(PageSerializer(pg).data,status=status.HTTP_201_CREATED)
    return Response("Serialization is invalid")

#====================================================================================================