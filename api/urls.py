from django.urls import path
from .views import CarView, CreateCarView, GetCar, GetPage, GetImage, CreateImageView, ViewImagesView

urlpatterns = [
    path('view-cars/', CarView.as_view()),
    path('create-car/', CreateCarView.as_view()),
    path('get-car/', GetCar.as_view()),
    path('pages/', GetPage.as_view()),
    path('get-image/', GetImage.as_view()),
    path('create-image/', CreateImageView.as_view()),
    path('view-images/', ViewImagesView.as_view())
]