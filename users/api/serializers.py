from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, CharField


class UserCreateSerializer(ModelSerializer):
    password1 = CharField(
        label="Password", style={"input_type": "password"}, write_only=True
    )
    password2 = CharField(
        label="Confirm Password", style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]
        extra_kwargs = {"password1": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]

        new_user = User(username=username, email=email)

        password1 = validated_data["password1"]
        password2 = validated_data["password2"]

        if password1 != password2:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        new_user.set_password(password1)

        new_user.save()

        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(read_only=True)
    username = CharField()
    password1 = CharField(
        label="Password", style={"input_type": "password"}, write_only=True
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "token",
        ]
