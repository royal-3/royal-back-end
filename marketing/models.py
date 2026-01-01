from django.db import models

class GallerySection(models.Model):
    title = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    section = models.ForeignKey(GallerySection, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    
    def __str__(self):
        return f"Image for {self.section.title}"

class ConsultationRequest(models.Model):
    HOUSE_TYPES = [
        ('1BHK', '1 BHK'),
        ('2BHK', '2 BHK'),
        ('3BHK', '3 BHK'),
        ('4BHK/Duplex', '4 BHK / Duplex'),
    ]
    PROPERTY_TYPES = [
        ('Commercial', 'Commercial'),
        ('Domestic', 'Domestic'),
    ]
    CITY_CHOICES = [
        ('Kalyani', 'Kalyani'),
        ('Kancharapara', 'Kancharapara'),
        ('Barrackpore', 'Barrackpore'),
        ('Naihati', 'Naihati'),
        ('Krishnanagar', 'Krishnanagar'),
        ('Kolkata', 'Kolkata'),
    ]
    name = models.CharField(max_length=255)
    house_type = models.CharField(max_length=20, choices=HOUSE_TYPES)
    city = models.CharField(max_length=100, choices=CITY_CHOICES)
    phone_number = models.CharField(max_length=15)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation for {self.name} - {self.city}"

class RecentWork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class RecentWorkImage(models.Model):
    project = models.ForeignKey(RecentWork, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recent_works/')

    def __str__(self):
        return f"Image for {self.project.title}"

class HeroSection(models.Model):
    image = models.ImageField(upload_to='hero/')
    title = models.CharField(max_length=255, default='ROYAL TOUCHUP')
    subtitle = models.CharField(max_length=255, default='Comfort Meets Creativity')
    description = models.TextField(default='We design spaces that feel good and work well. Personalized interior design tailored to your taste, lifestyle, and budget.')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Hero Section Config"

class Review(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField(default=5, help_text="Rating from 1 to 5")
    comment = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"
