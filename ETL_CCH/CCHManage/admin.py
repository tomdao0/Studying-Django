from django.contrib import admin
from .models import CLIENT, CLIENTCRS, STAFF


class CLIENTADMIN(admin.ModelAdmin):
    list_display = [
        "ClientIdSubId",
        "ClientSortName",
        "ClientStatus",
        "Created_Date",
        # "ETL_CCH__FirmClientStaffAssignmentName",
    ]
    list_filter = ["ClientStatus"]
    search_fields = ["ClientIdSubId", "ClientSortName"]


class CLIENTCRSADMIN(admin.ModelAdmin):
    list_display = [
        "ClientIdSubId",
        "StaffId",
        "FirmClientStaffAssignmentName",
    ]


# Register your models here.
admin.site.register(CLIENT, CLIENTADMIN)
admin.site.register(CLIENTCRS, CLIENTCRSADMIN)
admin.site.register(STAFF)
