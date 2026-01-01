from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GallerySectionViewSet, ConsultationRequestViewSet, RecentWorkViewSet, HeroSectionViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'gallery', GallerySectionViewSet)
router.register(r'consultation', ConsultationRequestViewSet)
router.register(r'recent-works', RecentWorkViewSet)
router.register(r'hero', HeroSectionViewSet, basename='hero')
router.register(r'reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
]
