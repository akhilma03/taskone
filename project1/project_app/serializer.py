from rest_framework import serializers
from .models import Product,ColourModel,productImage

class ColourModelSeralizer(serializers.ModelSerializer):
    class Meta:
        model=ColourModel
        fields='__all__'

class productImageSeralizer(serializers.ModelSerializer):
    class Meta:
        model=productImage
        fields='__all__'        


class productSerializer(serializers.ModelSerializer):
    color=ColourModelSeralizer(many=True,read_only=True)
    image=productImageSeralizer(many=True,read_only=True)
    class Meta:
        model =Product
        fields = '__all__'

