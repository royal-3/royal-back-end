from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GallerySectionViewSet, ConsultationRequestViewSet, RecentWorkViewSet

router = DefaultRouter()
router.register(r'gallery', GallerySectionViewSet)
router.register(r'consultation', ConsultationRequestViewSet)
router.register(r'recent-works', RecentWorkViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
