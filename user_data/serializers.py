from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'confirm_password', 'profile_image', 'bio', 'birthdate', 'birth_time']
        extra_kwargs = {
            'password': {'write_only': True},
            'confirm_password': {'write_only': True},
            'profile_image': {'required': False},
            'bio': {'required': False},
            'birthdate': {'required': False},
            'birth_time': {'required': False}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError('Passwords do not match.')
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create(**validated_data)
