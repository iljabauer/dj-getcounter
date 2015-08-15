from django.contrib import admin
from getcounter import models


class GetCounterAdmin(admin.ModelAdmin):
    list_display = ("parameter", "creation_date")
    list_filter = ("parameter",)


admin.site.register(models.GetCounter, GetCounterAdmin)
