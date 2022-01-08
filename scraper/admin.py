from django.contrib import admin
from .models import ScrapingSearch, ScrapingResult

class ScrapingResultAdmin(admin.ModelAdmin):
    pass

class ScrapingSearchAdmin(admin.ModelAdmin):
    pass

admin.site.register(ScrapingResult, ScrapingResultAdmin)
admin.site.register(ScrapingSearch, ScrapingSearchAdmin)