from django.contrib import admin
from .models import PackageRequest


@admin.register(PackageRequest)
class AdminForPackageRequest(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")


# admin.site.register(AnotherModel)
