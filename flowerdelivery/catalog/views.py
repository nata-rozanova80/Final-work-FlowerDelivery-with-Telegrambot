from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Products
from .serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
