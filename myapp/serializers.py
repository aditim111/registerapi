from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Hi

class HiSerializer(serializers.ModelSerializer):
    receiver  = serializers.CharField(source='receiver.username',read_only=True)
    sender  = serializers.CharField(source='sender.username',read_only=True)
    class Meta:
        model = Hi
        fields = ('receiver', 'sender','date')
class RegistrationSerializer (serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    class Meta:
        model = User
        fields = ('username','password')