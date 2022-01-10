from django.contrib import admin
from .models import BookRecord, Employee, Record, User, EmpLeaveRequests, Notification, Tickets, Book
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from django.contrib.auth.admin import UserAdmin

class RecordResource(resources.ModelResource):
    class Meta:
        model = Record

class RecordAdmin(ImportExportActionModelAdmin):
    resource_class = RecordResource
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ('name', 'department')
    ordering = ['department', 'name']
    
admin.site.register(User, UserAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Record, RecordAdmin)
admin.site.register(EmpLeaveRequests)
admin.site.register(Notification)
admin.site.register(Tickets)
admin.site.register(Book)
admin.site.register(BookRecord)