from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from common.enums import UserTypeChoices


class CommonUserSerializer(UserCreateSerializer):
    phone = serializers.CharField(max_length=24, required=False)
    profile_image = serializers.ImageField(required=False)
    user_type = serializers.ChoiceField(
        choices=UserTypeChoices.choices,
        default=UserTypeChoices.ADMIN,
        required=False,
    )

    class Meta(UserCreateSerializer.Meta):
        fields = [
            "email",
            "phone",
            "first_name",
            "last_name",
            "profile_image",
            "user_type",
        ]