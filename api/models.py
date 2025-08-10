from django.db import models

class TarotCard(models.Model):
    SUITE_CHOICES = [
        ('cups', 'Cups'),
        ('wands', 'Wands'),
        ('swords', 'Swords'),
        ('pentacles', 'Pentacles'),
        ('major', 'Major Arcana'),
    ]
    
    ELEMENT_CHOICES = [
        ('fire', 'Fire'),
        ('water', 'Water'),
        ('air', 'Air'),
        ('earth', 'Earth'),
    ]
    
    ASTROLOGICAL_SIGN_CHOICES = [
        ('aries', 'Aries'),
        ('taurus', 'Taurus'),
        ('gemini', 'Gemini'),
        ('cancer', 'Cancer'),
        ('leo', 'Leo'),
        ('virgo', 'Virgo'),
        ('libra', 'Libra'),
        ('scorpio', 'Scorpio'),
        ('sagittarius', 'Sagittarius'),
        ('capricorn', 'Capricorn'),
        ('aquarius', 'Aquarius'),
        ('pisces', 'Pisces'),
    ]
    
    PLANET_CHOICES = [
        ('sun', 'Sun'),
        ('moon', 'Moon'),
        ('mercury', 'Mercury'),
        ('venus', 'Venus'),
        ('mars', 'Mars'),
        ('jupiter', 'Jupiter'),
        ('saturn', 'Saturn'),
        ('uranus', 'Uranus'),
        ('neptune', 'Neptune'),
        ('pluto', 'Pluto'),
    ]
    
    title = models.CharField(max_length=100, verbose_name="Card Title")
    suite = models.CharField(max_length=20, choices=SUITE_CHOICES, verbose_name="Suite")
    number = models.PositiveIntegerField(null=True, blank=True, verbose_name="Card Number")
    image = models.ImageField(upload_to='tarot_cards/', verbose_name="Card Image")
    upright_meaning = models.TextField(verbose_name="Upright Meaning")
    reversed_meaning = models.TextField(verbose_name="Reversed Meaning")
    
    # Correspondences (optional fields)
    element = models.CharField(max_length=20, choices=ELEMENT_CHOICES, null=True, blank=True, verbose_name="Element")
    astrological_sign = models.CharField(max_length=20, choices=ASTROLOGICAL_SIGN_CHOICES, null=True, blank=True, verbose_name="Astrological Sign")
    planet = models.CharField(max_length=20, choices=PLANET_CHOICES, null=True, blank=True, verbose_name="Planet")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['suite', 'number', 'title']
        unique_together = ['suite', 'number']  # Prevent duplicate cards
    
    def __str__(self):
        if self.number:
            return f"{self.number} of {self.get_suite_display()}: {self.title}"
        return f"{self.title} ({self.get_suite_display()})"
