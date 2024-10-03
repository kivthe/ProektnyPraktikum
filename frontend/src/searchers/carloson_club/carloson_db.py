import requests
from bs4 import BeautifulSoup
import sqlite3

base_url = "https://carloson.ru/car"

# Заголовки для имитации запроса от браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

response = requests.get(base_url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Найти все ссылки на автомобили
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

# Создание подключения к базе данных SQLite
conn = sqlite3.connect('carloson_cars.db')
cursor = conn.cursor()

# Создание таблицы для хранения данных о автомобилях
cursor.execute('''
CREATE TABLE IF NOT EXISTS cars (
    link TEXT PRIMARY KEY,
    engine_volume TEXT,
    power TEXT,
    year TEXT,
    fuel_type TEXT,
    drive_type TEXT,
    img TEXT
)
''')

# Вставка данных в таблицу с пропуском дубликатов
for car in all_car_info:
    cursor.execute('''
    INSERT OR IGNORE INTO cars (link, engine_volume, power, year, fuel_type, drive_type, img)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (car['link'], car.get('engine_volume', 'Неизвестно'), car.get('power', 'Неизвестно'), car.get('year', 'Неизвестно'), car.get('fuel_type', 'Неизвестно'), car.get('drive_type', 'Неизвестно'), car['img']))

# Сохранение изменений и закрытие соединения
conn.commit()

cursor.close()
conn.close()

# Вывести всю собранную информацию
for car in all_car_info:
    print(f"Ссылка: {car['link']}")
    print(f"Объем двигателя: {car.get('engine_volume', 'Неизвестно')}")
    print(f"Мощность: {car.get('power', 'Неизвестно')}")
    print(f"Год выпуска: {car.get('year', 'Неизвестно')}")
    print(f"Тип топлива: {car.get('fuel_type', 'Неизвестно')}")
    print(f"Тип привода: {car.get('drive_type', 'Неизвестно')}")
    print(f"Ссылка на картинку: {car['img']}")
    print("---")
