from rest_framework import viewsets,status,filters
from rest_framework.permissions import IsAuthenticated,AllowAny
from .permissions import AdminOrReadOnly
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .pagination import CustomPagination



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']  
    pagination_class = CustomPagination
    
    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [AdminOrReadOnly]
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        price = request.data.get('price')
        if price and float(price) < 1.00:
            # raise ValidationError({"price": "Price must be at least $1.00."})
            raise Response({"price": "Price must be at least $1.00."}, status=status.HTTP_400_BAD_REQUEST)
        
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        quantity = request.data.get('quantity')
        if quantity and int(quantity) < 0:
            raise ValidationError({"quantity": "Quantity cannot be negative or zero."})
        
        return super().update(request, *args, **kwargs)

    
