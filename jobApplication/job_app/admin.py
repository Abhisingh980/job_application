from django.contrib import admin

from .models import Form


class FormsAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email",)
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("data", "occupation")
    ordering = ("first_name",)
    readonly_fields = ("occupation", "data", "email")


admin.site.register(Form, FormsAdmin)
