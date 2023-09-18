from rest_framework import serializers
from .models import UserProfile, Customer, Test

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email','name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            validated_data['email'],
            validated_data['name'],
            validated_data['password']
        )

        return user


# Customer Serializer
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')



# Test Serializer
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ('__all__')