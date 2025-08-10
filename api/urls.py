from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cards', views.TarotCardViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('health/', views.health_check, name='health_check'),
    path('reading/', views.tarot_reading, name='tarot_reading'),
    path('manage/', views.card_management, name='card_management'),
    path('search/', views.search_cards, name='search_cards'),
    path('draw-three/', views.draw_three_cards, name='draw_three_cards'),
    path('draw-ten/', views.draw_ten_cards, name='draw_ten_cards'),
]
