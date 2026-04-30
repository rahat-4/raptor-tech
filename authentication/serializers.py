from django.db import transaction
from rest_framework import serializers
from djoser.conf import settings
from djoser.serializers import UserCreateSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from authentication.models import User
from common.enums import UserTypeChoices
from common.serializers import CommonUserSerializer

class CustomUserCreateSerializer(UserCreateSerializer):
    # Fields for the required information during registration
    phone = serializers.CharField(max_length=24, required=False)
    profile_image = serializers.ImageField(required=False)
    designation = serializers.CharField(max_length=24, required=False)
    user_type = serializers.ChoiceField(
        choices=UserTypeChoices.choices,
        default=UserTypeChoices.ADMIN,
        required=False,
    )

    class Meta(UserCreateSerializer.Meta):
        fields = [
            "id",
            "email",
            "phone",
            "first_name",
            "last_name",
            "profile_image",
            "designation",
            "user_type",
            "password",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        

        # Extract user data
        password = validated_data.pop("password")

        with transaction.atomic():
            # Create the user
            user = User(**validated_data)
            user.set_password(password)



            user.save()

        return user

    def update(self, instance, validated_data):
        # Check if the request context has a user


        with transaction.atomic():
            # Update user fields
            for attr, value in validated_data.items():
                if attr == "password":
                    instance.set_password(value)
                else:
                    setattr(instance, attr, value)



            instance.save()

        return instance


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "profile_image",
            "designation",
            "user_type",
            "is_active",
            "is_staff",
            "created_at",
            "updated_at"
        ]

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["user_type"] = user.user_type
        token["email"] = user.email
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name

        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        request = self.context.get("request")

        if self.user.profile_image and request:
            profile_image_url = request.build_absolute_uri(self.user.profile_image.url)
        else:
            profile_image_url = None

        data["user"] = {  # type: ignore
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "email": self.user.email,
            "user_type": self.user.user_type,
            "profile_image": profile_image_url,
        }

        return data