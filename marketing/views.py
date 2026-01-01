from rest_framework import viewsets
from django.shortcuts import render
from .models import GallerySection, ConsultationRequest, RecentWork, HeroSection, Review
from .serializers import (
    GallerySectionSerializer,
    ConsultationRequestSerializer,
    RecentWorkSerializer,
    HeroSectionSerializer,
    ReviewSerializer
)

def home(request):
    return render(request, 'home.html')

class GallerySectionViewSet(viewsets.ModelViewSet):
    queryset = GallerySection.objects.all()
    serializer_class = GallerySectionSerializer

class ConsultationRequestViewSet(viewsets.ModelViewSet):
    queryset = ConsultationRequest.objects.all()
    serializer_class = ConsultationRequestSerializer

class RecentWorkViewSet(viewsets.ModelViewSet):
    queryset = RecentWork.objects.all()
    serializer_class = RecentWorkSerializer

class HeroSectionViewSet(viewsets.ModelViewSet):
    queryset = HeroSection.objects.filter(is_active=True)
    serializer_class = HeroSectionSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.filter(is_approved=True).order_by('-created_at')
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        # Auto-approve for now, or set to False if you want moderation
        serializer.save(is_approved=True)

