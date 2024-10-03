import requests
from bs4 import BeautifulSoup
from .models import RentrideCar
from .serializers import RentrideCarSerializer
import json

#====================================================================================================

class Rentride:

#====================================================================================================

  def find_info_rentride(url):
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive',
      'Upgrade-Insecure-Requests': '1',
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Найти все блоки с характеристиками автомобиля
    car_params_groups = soup.find_all('div', class_='CarParamsGroup')
    if len(car_params_groups) >= 2:
      second_group = car_params_groups[1]
      car_info = {}
      # Найти все элементы с характеристиками автомобиля
      car_params_items = second_group.find_all('div', class_='CarParamsGroupItem')
      for item in car_params_items:            
        name = item.find('div', class_='CarParamsGroupItem__name').text.strip()
        value = item.find('div', class_='CarParamsGroupItem__value').text.strip()
        car_info[name] = value
      try:
        del car_info["Мест"]
      finally:
        return car_info        
    else:
        return None

#====================================================================================================

  def search(self):
    base_url = "https://rentride.ru/arendovat/moskva/?page="
    total_pages = 24
    # Заголовки для имитации запроса от браузера
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
      'Accept-Language': 'en-US,en;q=0.5',
      'Accept-Encoding': 'gzip, deflate, br',
      'Connection': 'keep-alive',
      'Upgrade-Insecure-Requests': '1',
    }
    all_links = []
    with open("rentride_cars.txt", "w") as f:
      for page in range(1, total_pages + 1):
        url = f"{base_url}{page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        # Найти все ссылки на автомобили
        car_links = soup.find_all('a', class_='car-card-vertical')
        for link in car_links:
          href = link.get('href')
          if href:
            full_link = f"https://rentride.ru{href}"
            all_links.append(full_link)
            car_info = self.find_info_rentride(full_link)
            if car_info:
              # Вставка данных в таблицу с пропуском дубликатов
              if len(RentrideCar.objects.filter(link=full_link)) < 1:
                new_car = RentrideCar(link=full_link,
                                      engine=car_info.get('Двигатель','Unknown'),
                                      drive=car_info.get('Привод','Unknown'),
                                      year=car_info.get('Год','Unknown'))
                new_car.save()

    
#====================================================================================================

  def save_to_file():
    filename = "json_with_cars.json"
    all_cars = RentrideCar.objects.all()
    for car in all_cars:
      data = RentrideCarSerializer(car).data
      with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

#====================================================================================================

  def print_info():
    cars = RentrideCar.objects.all()
    for car in cars:
      print(f"Ссылка: {car.link}")
      print(f"Двигатель: {car.engine}")
      print(f"Тип привода: {car.drive}")
      print(f"Год выпуска: {car.year}")
      print("---")

#====================================================================================================