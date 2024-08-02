from rest_framework import viewsets
from .models import Product, Stock
from .serializers import ProductSerializer, ProductPositionSerializer
from rest_framework.pagination import
from .filter import ProductFilter
from django_filters import rest_framework as filters

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = ProductFilter


class StockViewSet(viewsets.ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = ProductPositionSerializer
