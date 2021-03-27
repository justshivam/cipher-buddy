from django.contrib import admin
from . import models


class EmailAdmin(admin.ModelAdmin):
    pass


class ComplaintAdmin(admin.ModelAdmin):
    pass


class ContactAdmin(admin.ModelAdmin):
    pass


class SiteComplaintsAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Email, EmailAdmin)
admin.site.register(models.Complaint, ComplaintAdmin)
admin.site.register(models.Contact, ContactAdmin)
admin.site.register(models.SiteComplaint, SiteComplaintsAdmin)
