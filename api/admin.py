from django.contrib import admin
from .models import TarotCard

@admin.register(TarotCard)
class TarotCardAdmin(admin.ModelAdmin):
    list_display = ['title', 'suite', 'number', 'element', 'astrological_sign', 'planet', 'created_at']
    list_filter = ['suite', 'element', 'astrological_sign', 'planet', 'created_at']
    search_fields = ['title', 'upright_meaning', 'reversed_meaning']
    ordering = ['suite', 'number', 'title']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'suite', 'number', 'image')
        }),
        ('Meanings', {
            'fields': ('upright_meaning', 'reversed_meaning')
        }),
        ('Correspondences (Optional)', {
            'fields': ('element', 'astrological_sign', 'planet'),
            'classes': ('collapse',),
        }),
    )
