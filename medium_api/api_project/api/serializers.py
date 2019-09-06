from rest_framework import serializers
from api.models import UserInformation

# Serializers define the API representation.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','last_name','age']


   