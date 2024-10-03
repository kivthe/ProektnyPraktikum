const express = require('express');
const path = require('path');
const cors = require('cors');
const app = express();
const PORT = 3001;

// Используем middleware для CORS
app.use(cors());

// Путь к вашему JSON файлу
const jsonFilePath = path.join(__dirname, 'json_with_cars.json');

// Маршрут для получения JSON файла
app.get('/data', (req, res) => {
  res.sendFile(jsonFilePath);
});

// Запуск сервера
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
