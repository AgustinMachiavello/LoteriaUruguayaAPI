"""Game serializer."""

# Django REST Framework
from rest_framework import serializers

# Models
from ..models.games import Game


class GameModelSerializer(serializers.ModelSerializer):
    """Game model serializer."""

    class Meta:
        """Meta class."""

        model = Game
        fields = '__all__'