from .models import CarlosonCar
from bs4 import BeautifulSoup
import requests
from .serializers import CarlosonCarSerializer
import json

class Carloson:
  def search():
    base_url = "https://carloson.ru/car"
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive',
      'Upgrade-Insecure-Requests': '1',
    }
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    car_links = soup.find_all('a', class_='col-xl-4 col-lg-4 col-md-6 col-sm-6 col-12 mb-2 mb-md-4')
    all_car_info = []
    for link in car_links:
      car_info = {}
      car_info['link'] = link.get('href')
      # Найти информацию о автомобиле
      image_link = link.find("div", class_="img__box").find("img").get("src")
      info_div = link.find('div', class_='two__block_slide__text__bottom')
      if info_div:
        info_spans = info_div.find_all('span')
        # Проверка на электрический двигатель
        if info_spans[2].text.strip().lower() == 'электро':
          car_info['engine_volume'] = '-'
          car_info['power'] = info_spans[0].text.strip()
          car_info['year'] = info_spans[1].text.strip()
          car_info['fuel_type'] = info_spans[2].text.strip()
          car_info['drive_type'] = info_spans[3].text.strip()
          car_info['img'] = image_link
        else:
          if len(info_spans) > 4:
            car_info['engine_volume'] = info_spans[0].text.strip()
            car_info['power'] = info_spans[1].text.strip()
            car_info['year'] = info_spans[2].text.strip()
            car_info['fuel_type'] = info_spans[3].text.strip()
            car_info['drive_type'] = info_spans[4].text.strip()
            car_info['img'] = image_link
          else:
            car_info['engine_volume'] = info_spans[0].text.strip()
            car_info['power'] = info_spans[1].text.strip()
            car_info['year'] = info_spans[2].text.strip()
            car_info['fuel_type'] = info_spans[3].text.strip()
            car_info['drive_type'] = "-"
            car_info['img'] = image_link
      all_car_info.append(car_info)
    for car in all_car_info:
      sorted = CarlosonCar.objects.filter(link=car['link'])
      if len(sorted) < 1:
        new_car = CarlosonCar(link=car['link'],
                              engine_volume=car.get('engine_volume','Unknwon'),
                              power=car.get('power', 'Unknown'),
                              year=car.get('year', 'Unknown'),
                              fuel_type=car.get('fuel_type', 'Unknown'),
                              drive_type=car.get('drive_type', 'Unknown'),
                              img=car['img'])
        new_car.save()

  def save_to_file():
    filename = "json_with_carloson.json"
    all_cars = CarlosonCar.objects.all()
    for car in all_cars:
      data = CarlosonCarSerializer(car).data
      with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

  def print_info():
    cars = CarlosonCar.objects.all()
    for car in cars:
      print(f"Ссылка: {car.link}")
      print(f"Объем двигателя: {car.engine_volume}")
      print(f"Мощность: {car.power}")
      print(f"Год выпуска: {car.year}")
      print(f"Тип топлива: {car.fuel_type}")
      print(f"Тип привода: {car.drive_type}")
      print(f"Ссылка на картинку: {car.img}")
      print("---")