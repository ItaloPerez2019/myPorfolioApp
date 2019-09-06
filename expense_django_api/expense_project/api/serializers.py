from rest_framework import serializers, exceptions

from django.contrib.auth import authenticate

from expense.models import Expense, UserLogin
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get("username", "")
        password = data.get("password", "")

        if username and password:
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    data["user"] = user
                else:
                    msg = "User is deactivated"
                    raise exceptions.ValidationError(msg)

            else:
                msg = "Unable to login with given credetials"
                raise exceptions.ValidationError(msg)
        else:
            msg = "please provide username and password "
            raise exceptions.ValidationError(msg)
        return data





    # class Meta:
    #     model = User
    #     fields = ('username', 'password')

# class LoginSerializer(serializers.ModelSerializer):
#
#     class Meta:
#             model = User
#             fields = ('username', 'password')


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ( 'user', 'description', 'amount', 'types')


