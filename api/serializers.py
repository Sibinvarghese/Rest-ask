from rest_framework.serializers import ModelSerializer
from .models import UserRegistration,CustomerSupport

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=UserRegistration
        fields=["Firstname","Lastname","Email_address","Password","Role"]

class CustomerSupportSerializer(ModelSerializer):
    class Meta:
        model=CustomerSupport
        fields=["user_id","message","ticket_id","status"]

