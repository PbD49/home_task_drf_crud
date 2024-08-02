from django_filters import rest_framework as filters
from .models import Product


class ProductFilter(filters.filterset):
    class Meta:
        model = Product
        fields = ["title", "description",]
