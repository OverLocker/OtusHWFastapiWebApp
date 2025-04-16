Запуск:
uvicorn app.main:app --reload

Получить список товаров:
GET http://127.0.0.1:8000/api/products/

Получить товар по ID: 
GET http://127.0.0.1:8000/api/products/{product_id}

Создать новый товар: 
POST http://127.0.0.1:8000/api/products/ (с телом запроса в формате JSON)

Пример запроса на создание:
curl -X POST "http://127.0.0.1:8000/api/products/" \
-H "Content-Type: application/json" \
-d '{
  "id": 1,
  "name": "Laptop",
  "description": "A Super Laptop.",
  "price": 1094.94
}'
