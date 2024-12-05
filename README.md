# Final-work-FlowerDelivery-with-Telegrambot
Итоговая работа по окончании курса "Python-разработчик" 

Для работы с ViewSet вы можете обращаться к нему через API, например:

GET: /api/products/ — получить список всех продуктов.
POST: /api/products/ — создать новый продукт.
GET: /api/products/<id>/ — получить продукт по ID.
PUT/PATCH: /api/products/<id>/ — обновить продукт.
DELETE: /api/products/<id>/ — удалить продукт.


Разбор кода:
DefaultRouter(): Создается объект роутера, который будет генерировать маршруты для API.

router.register(r'products', ProductViewSet): Регистрируем ViewSet ProductViewSet для маршрута /products/:

r'products' — базовый URL-адрес для этого ViewSet.
ProductViewSet — класс, который обрабатывает запросы для этого маршрута.
urlpatterns += router.urls: Генерируемые маршруты добавляются к списку urlpatterns, чтобы они стали доступны для приложения.

Пример сгенерированных маршрутов
При регистрации ProductViewSet с роутером будут созданы следующие маршруты:

HTTP Метод	URL	Описание
GET	/products/	Получить список всех продуктов
POST	/products/	Создать новый продукт
GET	/products/<id>/	Получить данные конкретного продукта
PUT	/products/<id>/	Полностью обновить продукт
PATCH	/products/<id>/	Частично обновить продукт
DELETE	/products/<id>/	Удалить продукт