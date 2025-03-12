from django.contrib import admin

from Employee_Note.models import EmployeeInfo, Locations, PhoneNumbers, Campaign, CampaignDetails


class LocationsAdmin(admin.ModelAdmin):
    list_display = ['unique_locations']


admin.site.register(Locations)


class EmployeeInfoAdmin(admin.ModelAdmin):
    list_display = ['emp_name', 'emp_location', 'emp_phone']


admin.site.register(EmployeeInfo)


class PhoneNumbersAdmin(admin.ModelAdmin):
    list_display = ['employee_data']


admin.site.register(PhoneNumbers)

admin.site.register(Campaign)
admin.site.register(CampaignDetails)
