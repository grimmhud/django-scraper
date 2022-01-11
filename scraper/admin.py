from django.contrib import admin
from .models import ScrapingSearch, ScrapingResult
from .services.AdminServices import ExportCsvMixin

@admin.register(ScrapingResult)
class ScrapingResultAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]


@admin.register(ScrapingSearch)
class ScrapingSearchAdmin(admin.ModelAdmin):
    pass