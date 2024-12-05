from django.urls import path, include
from rest_framework.routers import DefaultRouter # Импорт роутера
from .views import ProductViewSet # Импорт ViewSet

# Создаем роутер и регистрируем ViewSet
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

# Подключаем маршруты роутера
urlpatterns = [
    path('', include(router.urls)),  # Включаем маршруты роутера
    path('api/', include('catalog.urls')),  # Подключаем маршруты приложения
]

urlpatterns += router.urls  # Добавляем маршруты из роутера




