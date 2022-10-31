from django.contrib import admin

from.models import  xinwen

class XinwenAdmin(admin.ModelAdmin):
    search_fields = ["biaoti","zuozhe"]
    list_display = ["biaoti","zuozhe","neirong"]

admin.site.register(xinwen,XinwenAdmin)
