from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from nemesis.models import Users

class RegFormSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    confirm_password=serializers.CharField(write_only=True)
    class Meta:
        model=Users
        fields=['username','email','password','confirm_password','address']
        extra_kwargs = {"confirm password": {"write_only": True},"password": {"write_only": True}}
    
    def create(self,validated_data):
        print("in create")
        password=validated_data.pop('password')
        confirm_password=validated_data.pop('confirm_password')
        instance=self.Meta.model(**validated_data)
        print("instance",instance)
        if password is not None:
            if password!=confirm_password:
                print(password,confirm_password)
                raise serializers.ValidationError("Password and Confirm_password  do not Match")
            else:
                instance.set_password(password)
                instance.save()
        return instance



        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id','username', 'email','address')