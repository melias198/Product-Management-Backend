from django.urls import path,include
from .views import ProductViewSet
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
SpectacularAPIView, 
SpectacularSwaggerView, 
)

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"), 
    path("doc/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"), 
]