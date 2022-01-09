from django.http import HttpResponse
from .FileConverter import to_csv

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