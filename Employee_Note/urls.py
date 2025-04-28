from django.urls import path

from Employee_Note import views

urlpatterns = [
    path('menu/', views.menu_page, name='menu_page'),
    path('menu/info/', views.display_employee_info, name='employee_info'),
    path('menu/info/preview/', views.preview_page, name='preview'),
    path('menu/report/', views.report_page, name='report'),
    path('report-info/', views.report_info, name='report_info'),

    path('populate/', views.generate_employee_data, name='generate_employee_data'),

    path('api-get-loc/', views.fetching_locations, name='get_locations'),
    path('api-get-emp-details/', views.employee_details, name='get_employee_details'),
    path('api-add-campaign/', views.add_campaign_data, name='add_campaign'),
    path('api-campaign-report/', views.fetch_campaign_info, name='campaign_report'),


]
