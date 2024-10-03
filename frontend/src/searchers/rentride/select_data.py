import sqlite3
import json

connection = sqlite3.connect('rentride_cars.db')
cursor = connection.cursor()

cursor.execute("SELECT * FROM cars")
table = cursor.fetchall()

table_new = []
element_new = {}

for table_string in table:
    element_new.update(
        url=table_string[0],
        engine_volume=table_string[1],
        power=table_string[2],
        year=table_string[3],
        fuel_type=table_string[4],
        drive_type=table_string[5],
        image=table_string[6]
        )

    table_new.append(element_new)
    element_new = {}
    
with open("json_with_cars.json", "w", encoding="utf-8") as file:
    json.dump(table_new, file, ensure_ascii=False, indent=4)
    
connection.commit()

cursor.close()
connection.close()
    