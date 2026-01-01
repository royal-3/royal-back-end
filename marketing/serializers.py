from rest_framework import serializers
from .models import GallerySection, GalleryImage, ConsultationRequest, RecentWork, RecentWorkImage, HeroSection, Review

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image']

class GallerySectionSerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)

    class Meta:
        model = GallerySection
        fields = ['id', 'title', 'images']

class ConsultationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultationRequest
        fields = '__all__'

class RecentWorkImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentWorkImage
        fields = ['id', 'image']

class RecentWorkSerializer(serializers.ModelSerializer):
    images = RecentWorkImageSerializer(many=True, read_only=True)

    class Meta:
        model = RecentWork
        fields = ['id', 'title', 'description', 'images']

class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
