
# Primero importamos los modelos que queremos serializar:
from e_commerce.models import Comic,WishList
from django.contrib.auth.models import User

from rest_framework import serializers

class ComicSerializer(serializers.ModelSerializer):
    # algo =  serializers.SerializerMethodField()
    
    class Meta:
        model = Comic
        fields = ('marvel_id','title', 'description', 'price', 'stock_qty', 'picture')
        # fields = ('marvel_id', 'title', 'algo')

    # def get_algo(self, obj):
    #     return {'hola':10}


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ("__all__")

# TODO: Realizar el serializador para el modelo de WishList