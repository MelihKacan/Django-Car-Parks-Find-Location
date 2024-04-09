from rest_framework import serializers
from .models import CarParkModel, CustomUser


class CarParkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length=100)
    capacity = serializers.FloatField()
    now_capaticy = serializers.FloatField()
    latitude = serializers.FloatField()   #Enlem
    longitude = serializers.FloatField()  #Boylam
    
class CustomUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password','email','phone_number']
        extra_kwargs = {"password":{"write_only" :  True}}
     
    def create_user(self,validated_data):
        user = CustomUser(
            username = validated_data["username"],
            email = validated_data["email"],
            phone = validated_data["phone_number"]
        )   
        user.set_password(validated_data["password"])
        user.save()
        return user
    