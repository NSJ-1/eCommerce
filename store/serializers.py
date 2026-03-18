from rest_framework import serializers
from .models import Store, Product

class StoreSerializer(serializers.ModelSerializer):
    """
    Serializer for the Store model.

    Converts Store model instances into JSON format and
    validates incoming data for creating/updating stores.
    """
    class Meta:
        model = Store
        fields = ['vendor', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Converts product model instances into JSON format and
    validates data that comes in for creating/updating products.
    """
    class Meta:
        model = Product
        fields = ['name', 'price', 'owner']
