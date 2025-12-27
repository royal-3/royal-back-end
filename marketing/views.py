from rest_framework import viewsets
from django.shortcuts import render
from .models import GallerySection, ConsultationRequest, RecentWork
from .serializers import (
    GallerySectionSerializer,
    ConsultationRequestSerializer,
    RecentWorkSerializer
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
