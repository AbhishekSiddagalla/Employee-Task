from django.contrib import admin
from Employee_Note.models import EmployeeInfo,Locations,PhoneNumbers,Report

class LocationsAdmin(admin.ModelAdmin):
    list_display = ['unique_locations']
admin.site.register(Locations)

class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ['emp_name','emp_location','emp_phone']
admin.site.register(EmployeeInfo)

class PhoneNumbersAdmin(admin.ModelAdmin):
    list_display = ['employee_data']
admin.site.register(PhoneNumbers)

admin.site.register(Report)