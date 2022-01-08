from django.contrib import admin
from .models import ScrapingSearch, ScrapingResult
import csv
from django.http import HttpResponse
from .services.FileConverter import to_csv
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)

        for obj in queryset:
            values = getattr(obj, 'values')
            to_csv(response, values)

        return response

    export_as_csv.short_description = "Export Data Selected"

@admin.register(ScrapingResult)
class ScrapingResultAdmin(admin.ModelAdmin, ExportCsvMixin):
    actions = ["export_as_csv"]


@admin.register(ScrapingSearch)
class ScrapingSearchAdmin(admin.ModelAdmin):
    pass