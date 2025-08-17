from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        # Remove confirm_password if present
        validated_data.pop('confirm_password', None)
        # Update all fields except profile_image
        for attr, value in validated_data.items():
            if attr != 'profile_image':
                setattr(instance, attr, value)
        # Handle profile_image separately
        profile_image = validated_data.get('profile_image', None)
        if profile_image:
            instance.profile_image = profile_image
        instance.save()
        return instance
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
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password is not None or confirm_password is not None:
            if password != confirm_password:
                raise serializers.ValidationError('Passwords do not match.')
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        return User.objects.create(**validated_data)
