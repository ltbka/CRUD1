from django.contrib.auth.models import User 
from rest_framework import serializers 
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class RegistrationSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True, required=True)
    password_confirmation = serializers.CharField(min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'password_confirmation')

    def validate(self, attrs):
        password_confirmation = attrs.pop('password_confirmation')
        if password_confirmation != attrs['password']:
            raise serializers.ValidationError('Пароли не совпадают')
        if not attrs['first_name'].istitle():
            raise serializers.ValidationError('Имена начинаются с большой буквы')
        
        return attrs

    def validate_password(self, value):
        try:
            validate_password(value)
        except serializers.ValidationError as error:
            raise serializers.ValidationError(str(error))

        return value


    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120)
    password = serializers.CharField(max_length=299)
    
    def validate(self, attrs):
        request = self.context.get('request')
        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:
            user = authenticate(
                username=username,
                password=password,
                request=request
            )
            if not user:
                raise serializers.ValidationError('Неверный username или password')
            
        else:
            raise serializers.ValidationError('username и password обязателен к заполнению!')
        
        attrs['user'] = user
        return attrs
    
    def validate_username(self, username):
        if not User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                'Пользователь с таким username не найден'
            )
        return username
        
        



