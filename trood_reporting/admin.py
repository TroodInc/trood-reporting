from django.contrib import admin

from .models import Report, Source


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    pass
