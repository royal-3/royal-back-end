from django.contrib import admin
from .models import GallerySection, GalleryImage, ConsultationRequest, RecentWork, RecentWorkImage

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

class GallerySectionAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]

class RecentWorkImageInline(admin.TabularInline):
    model = RecentWorkImage
    extra = 1

class RecentWorkAdmin(admin.ModelAdmin):
    inlines = [RecentWorkImageInline]

admin.site.register(GallerySection, GallerySectionAdmin)
admin.site.register(ConsultationRequest)
admin.site.register(RecentWork, RecentWorkAdmin)
