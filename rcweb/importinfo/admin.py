from django.contrib import admin
from importinfo.models import BaseInfo
from import_export import resources

class BaseAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        obj.save()

admin.site.register(BaseInfo, BaseAdmin)

# Register your models here.
