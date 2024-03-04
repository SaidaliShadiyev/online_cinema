from django.contrib import admin
from .models import *

class SlugAdmin(admin.ModelAdmin):
      prepopulated_fields = {"slug":('title',)}

admin.site.register(Film, SlugAdmin)
admin.site.register(Genre, SlugAdmin)

