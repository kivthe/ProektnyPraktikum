import requests
from bs4 import BeautifulSoup
import sqlite3

def find_info_rentride(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Найти все блоки с характеристиками автомобиля
    car_params_groups = soup.find_all('div', class_='CarParamsGroup')

    if len(car_params_groups) >= 2:
        second_group = car_params_groups[1]
        car_info = {}

        # Найти все элементы с характеристиками автомобиля
        car_params_items = second_group.find_all('div', class_='CarParamsGroupItem')
        print(car_params_items)

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

# Создание подключения к базе данных SQLite
conn = sqlite3.connect('rentride_cars.db')
cursor = conn.cursor()

# Создание таблицы для хранения данных о автомобилях
cursor.execute('''
CREATE TABLE IF NOT EXISTS cars (
    link TEXT PRIMARY KEY,
    engine TEXT,
    drive TEXT,
    year TEXT
)
''')

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
                print(full_link)
                car_info = find_info_rentride(full_link)
                if car_info:
                    print(car_info)
                    # Вставка данных в таблицу с пропуском дубликатов
                    cursor.execute('''
                    INSERT OR IGNORE INTO cars (link, engine, drive, year)
                    VALUES (?, ?, ?, ?)
                    ''', (full_link, car_info.get('Двигатель', 'Неизвестно'), car_info.get('Привод', 'Неизвестно'), car_info.get('Год', 'Неизвестно'))) # , car_info['img']
                print(full_link, file=f)

# Сохранение изменений и закрытие соединения
conn.commit()

cursor.close()
conn.close()

# Вывести все ссылки
# for link in all_links:
#     print(link)
