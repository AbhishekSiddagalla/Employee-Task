from django.urls import path

from Employee_Note import views

urlpatterns = [
    path('populate/', views.generate_employee_data, name='generate_employee_data'),
    path('info/', views.display_employee_info, name='employee_info'),
    path('api-get-loc/', views.fetching_locations, name='get_locations'),
    path('api-get-emp-details/', views.employee_details, name='get_employee_details'),
    path('preview/', views.preview_page, name='preview'),
    path('report/', views.report_page, name='report'),
    path('api-add-campaign/', views.add_campaign_data, name='add_campaign'),
    path('api-campaign-report/', views.fetch_campaign_info, name='campaign_report'),
    path('menu/', views.menu_page, name='menu_page'),
    path('report-info/', views.report_info, name='report_info'),
    # path('api-campaign-info/',views.get_campaign_details,name='campaign_details'),
]
