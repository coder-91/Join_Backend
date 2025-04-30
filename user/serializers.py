"""Serializers for the user API View."""
from django.db.models import Max
from django.utils import timezone
from rest_framework import serializers
from django.contrib.auth import (
    get_user_model,
    authenticate,
)
from django.utils.translation import gettext as _


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'password', 'name', 'phone_number', 'is_guest', 'date_joined', 'avatar_color']
        extra_kwargs = {
            'email': {'required': False},
            'password': {'required': False, 'write_only': True, 'style': {'input_type': 'password'}, 'min_length': 6},
            'name': {'required': False},
            'phone_number': {'required': False},
            'date_joined': {'read_only': True},
            'avatar_color': {'read_only': True}
        }

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        validated_data['date_joined'] = timezone.now()
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """Update and return user."""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class GuestSerializer(serializers.ModelSerializer):
    """Serializer for guests."""

    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'name', 'is_guest', 'date_joined', 'avatar_color']
        extra_kwargs = {
            'email': {'required': False},
            'name': {'required': False},
            'is_guest': {'default': True},
            'date_joined': {'read_only': True},
            'avatar_color': {'read_only': True}
        }

    def create(self, validated_data):
        """Create and return a guest user with default values."""
        user = get_user_model()
        max_id = user.objects.filter(is_guest=True).aggregate(max_id=Max('id'))['max_id']
        if max_id is None:
            guest_id = 1
        else:
            guest_id = max_id + 1

        validated_data['email'] = f'guest_{guest_id}@example.com'
        validated_data['name'] = f'Guest_{guest_id}'
        validated_data['is_guest'] = True
        validated_data['date_joined'] = timezone.now()
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
    )

    def validate(self, attrs):
        """Validate and authenticate the user."""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
