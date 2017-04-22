from django.contrib import admin

from .models import *


class ArtAdmin(admin.ModelAdmin):
    class Meta:
        model = Art


class ArtImagesAdmin(admin.ModelAdmin):
    class Meta:
        model = ArtImages


admin.site.register(Art, ArtAdmin)

admin.site.register(ArtImages, ArtImagesAdmin)
