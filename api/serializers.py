from rest_framework import serializers
from .models import TarotCard

class TarotCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarotCard
        fields = ['id', 'title', 'suite', 'number', 'image', 'upright_meaning', 'reversed_meaning', 
                 'element', 'astrological_sign', 'planet', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, data):
        # Custom validation for major arcana cards
        if data.get('suite') == 'major' and data.get('number') is not None:
            if not (0 <= data['number'] <= 21):
                raise serializers.ValidationError("Major Arcana cards should have numbers between 0-21")
        
        # Custom validation for minor arcana cards
        elif data.get('suite') in ['cups', 'wands', 'swords', 'pentacles'] and data.get('number') is not None:
            if not (1 <= data['number'] <= 14):
                raise serializers.ValidationError("Minor Arcana cards should have numbers between 1-14 (including Ace=1, Jack=11, Queen=12, King=13, Knight=14)")
        
        return data

class TarotCardCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TarotCard
        fields = ['title', 'suite', 'number', 'image', 'upright_meaning', 'reversed_meaning', 
                 'element', 'astrological_sign', 'planet']
    
    def validate(self, data):
        # Custom validation for major arcana cards
        if data.get('suite') == 'major' and data.get('number') is not None:
            if not (0 <= data['number'] <= 21):
                raise serializers.ValidationError("Major Arcana cards should have numbers between 0-21")
        
        # Custom validation for minor arcana cards
        elif data.get('suite') in ['cups', 'wands', 'swords', 'pentacles'] and data.get('number') is not None:
            if not (1 <= data['number'] <= 14):
                raise serializers.ValidationError("Minor Arcana cards should have numbers between 1-14")
        
        return data
