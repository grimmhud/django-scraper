from django.http import HttpResponse
from .FileConverter import create_csv, zipFiles

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=web-scraping.zip'

        csv_files = []
        for obj in queryset:
            values = getattr(obj, 'values')
            csv_files.append({'filename': f'scraping-id_{obj.id}', 'file': create_csv(values)})

        zipFiles(response, csv_files)
        return response

    export_as_csv.short_description = "Export Data Selected"