from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'department', 'status', 'hire_date')
    search_fields = ('first_name', 'last_name', 'email', 'department')
    list_filter = ('status', 'department')

# Alternatively, if using admin.site.register:
# admin.site.register(Employee, EmployeeAdmin)
