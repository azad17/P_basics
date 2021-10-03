from .models  import Books,Fruits
from rest_framework import serializers
from django.contrib.auth.models import User 

class UserSerializer(serializers.ModelSerializer):
    fruits = serializers.PrimaryKeyRelatedField(many=True,queryset=Fruits.objects.all())
    owner = serializers.ReadOnlyField(source ='owner.username')
    class Meta:
        model =User
        fields = ['id','username','fruits','owner']

class BookSerializer (serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = "__all__"

class FruitsSerializer (serializers.ModelSerializer):
    class Meta :
        model = Fruits
        fields = "__all__"



# class NewSerializer (serializers.Serializer):
#     name = serializers.CharField(read_only = True)
#     color = serializers.CharField(required = False,allow_blank = True,max_length= 100)
#     type = serializers.CharField(max_length = 100)
#     count = serializers.IntegerField()
    
    

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Fruits.objects.create(**validated_data)
    # def update(self, instance, validated_data):
    
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.code = validated_data.get('code', instance.code)
    #     instance.linenos = validated_data.get('linenos', instance.linenos)
    #     instance.language = validated_data.get('language', instance.language)
    #     instance.style = validated_data.get('style', instance.style)
    #     instance.save()
    #     return instance
