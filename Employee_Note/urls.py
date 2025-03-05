from django.urls import path
from Employee_Note import views
urlpatterns = [
    path('populate/',views.generate_employee_data, name = 'generate_employee_data'),
    path('info/',views.display_employee_info, name='employee_info'),
    path('api-get-loc/',views.get_unique_locations, name='get_locations'),
    path('api-get-emp-details/',views.get_employee_details, name='get_employee_details'),
    path('preview/', views.preview_page, name='preview'),
    path('report/',views.report_page,name='report'),
    path('api-add-campaign/', views.add_campaign_data,name='add_campaign'),
    path('api-campaign-report/',views.campaign_report,name='campaign_report'),

]