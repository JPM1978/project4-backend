from django.shortcuts import render
from .models import Deck
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import DeckSerializer
# Create your views here.

class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [permissions.AllowAny]
    
    