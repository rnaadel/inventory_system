from rest_framework import serializers
from .models import Shipments
from product.models import Product
from user.models import CustomUser

class ShipmentsSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Shipments
        fields = [ 'product_id', 'user_id', 'date_time', 'approved', 'shipped']

