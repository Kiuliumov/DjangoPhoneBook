from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from accounts.models import Account

User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = (
            "profile_picture",
            "phone",
            "gender",
            "bio",
        )


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    account = AccountSerializer()

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "account",
        )

    def validate_password(self, value):
        validate_password(value)
        return value

    @transaction.atomic
    def create(self, validated_data):
        account_data = validated_data.pop("account", {})

        user = User.objects.create_user(**validated_data)

        account = user.account

        account_serializer = AccountSerializer(
            account,
            data=account_data,
            partial=True,
        )
        account_serializer.is_valid(raise_exception=True)
        account_serializer.save()

        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )

        if not user:
            raise serializers.ValidationError("Invalid credentials.")

        refresh = RefreshToken.for_user(user)

        return {
            "user_id": user.id,
            "username": user.username,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
