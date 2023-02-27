from .models import Deck
from rest_framework import serializers

class DeckSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Deck
        fields = ['id', 'deck', 'cards']

