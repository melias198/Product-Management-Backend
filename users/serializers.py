from rest_framework import serializers
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        
        if password != password2:
            raise serializers.ValidationError({'error' : "Password Doesn't Matched."})
        
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'error' : "Username Already Exists!"})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already Exists!"})
        
        account = User(username = username, email=email, first_name = first_name, last_name = last_name)
        account.set_password(password)
        account.save()
        return account


class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()