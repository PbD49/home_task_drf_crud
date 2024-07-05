from rest_framework import routers
from logistic import views


router = routers.SimpleRouter()
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'stock', views.StockViewSet, basename='stock')


urlpatterns = router.urls
