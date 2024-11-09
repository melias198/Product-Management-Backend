from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']
        
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be more than $0.")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be zero or negative.")
        return value

    