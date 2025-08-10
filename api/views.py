from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from django.db.models import Q
import random
from .models import TarotCard
from .serializers import TarotCardSerializer, TarotCardCreateSerializer

class TarotCardViewSet(ModelViewSet):
    queryset = TarotCard.objects.all()
    serializer_class = TarotCardSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return TarotCardCreateSerializer
        return TarotCardSerializer

@api_view(['GET'])
def health_check(request):
    """
    Simple health check endpoint
    """
    return Response({'status': 'healthy', 'message': 'Tarot API is running'}, status=status.HTTP_200_OK)

@api_view(['GET'])
def tarot_reading(request):
    """
    Basic tarot reading endpoint (placeholder)
    """
    # This is a placeholder - you can expand this with actual tarot card logic
    sample_cards = [
        {'name': 'The Fool', 'meaning': 'New beginnings', 'position': 'past'},
        {'name': 'The Sun', 'meaning': 'Joy and success', 'position': 'present'},
        {'name': 'The Star', 'meaning': 'Hope and guidance', 'position': 'future'},
    ]
    
    return Response({
        'reading': sample_cards,
        'message': 'Your tarot reading'
    }, status=status.HTTP_200_OK)

def card_management(request):
    """
    Render the card management page with modal
    """
    return render(request, 'api/card_management.html')

@api_view(['GET'])
def search_cards(request):
    """
    Search for tarot cards by title, suite, or meanings
    """
    query = request.GET.get('q', '')
    
    if not query:
        return Response({
            'error': 'Please provide a search query using the "q" parameter'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Search across multiple fields
    cards = TarotCard.objects.filter(
        Q(title__icontains=query) |
        Q(suite__icontains=query) |
        Q(upright_meaning__icontains=query) |
        Q(reversed_meaning__icontains=query) |
        Q(element__icontains=query) |
        Q(astrological_sign__icontains=query) |
        Q(planet__icontains=query)
    ).distinct()
    
    serializer = TarotCardSerializer(cards, many=True)
    
    return Response({
        'query': query,
        'count': len(serializer.data),
        'results': serializer.data
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def draw_three_cards(request):
    """
    Draw 3 random cards without duplicates for a simple reading
    """
    all_cards = list(TarotCard.objects.all())
    
    if len(all_cards) < 3:
        return Response({
            'error': 'Not enough cards in the database. Need at least 3 cards to draw.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Randomly select 3 cards without replacement
    selected_cards = random.sample(all_cards, 3)
    
    # Create reading positions
    reading = []
    positions = ['Past', 'Present', 'Future']
    
    for i, card in enumerate(selected_cards):
        card_data = TarotCardSerializer(card).data
        # Randomly determine if card is upright or reversed
        is_reversed = random.choice([True, False])
        
        reading.append({
            'position': positions[i],
            'card': card_data,
            'orientation': 'reversed' if is_reversed else 'upright',
            'meaning': card_data['reversed_meaning'] if is_reversed else card_data['upright_meaning']
        })
    
    return Response({
        'reading_type': '3-Card Past/Present/Future Reading',
        'cards_drawn': 3,
        'reading': reading
    }, status=status.HTTP_200_OK)

@api_view(['GET'])
def draw_ten_cards(request):
    """
    Draw 10 random cards without duplicates for a Celtic Cross reading
    """
    all_cards = list(TarotCard.objects.all())
    
    if len(all_cards) < 10:
        return Response({
            'error': 'Not enough cards in the database. Need at least 10 cards to draw.'
        }, status=status.HTTP_400_BAD_REQUEST)
    
    # Randomly select 10 cards without replacement
    selected_cards = random.sample(all_cards, 10)
    
    # Celtic Cross positions
    positions = [
        'Present Situation',
        'Challenge/Cross',
        'Distant Past/Foundation',
        'Recent Past',
        'Possible Outcome',
        'Immediate Future',
        'Your Approach',
        'External Influences',
        'Inner Feelings',
        'Final Outcome'
    ]
    
    reading = []
    for i, card in enumerate(selected_cards):
        card_data = TarotCardSerializer(card).data
        # Randomly determine if card is upright or reversed
        is_reversed = random.choice([True, False])
        
        reading.append({
            'position': positions[i],
            'card': card_data,
            'orientation': 'reversed' if is_reversed else 'upright',
            'meaning': card_data['reversed_meaning'] if is_reversed else card_data['upright_meaning']
        })
    
    return Response({
        'reading_type': '10-Card Celtic Cross Reading',
        'cards_drawn': 10,
        'reading': reading
    }, status=status.HTTP_200_OK)
