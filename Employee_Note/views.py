import random

from django.http import JsonResponse
from django.shortcuts import render
from model_bakery import baker

from Employee_Note.forms import AddCampaignForm
from Employee_Note.models import EmployeeInfo, Locations, PhoneNumbers, Campaign


def generate_employee_data(request):
    """ Populating data for 1000 records """
    generated_data = []

    country_list = ["India", "USA", "UK", "Germany", "Australia",
                    "China", "Russia", "Japan", "New Zealand", "Canada"]

    for country in country_list:
        baker.make(Locations, unique_locations=country)

    for _ in range(100):
        emp_name = f"Employee{random.randint(1, 1000)}"  # Random employee name

        emp_location_name = random.choice(country_list)

        emp_phone = str(random.randint(1000000000, 9999999999))

        masked_phone = 'XXXXXX' + emp_phone[-4:]

        emp_location = Locations.objects.get(unique_locations=emp_location_name)

        emp_info = baker.make(EmployeeInfo,
                              emp_name=emp_name,
                              emp_location=emp_location,
                              emp_phone=masked_phone)

        baker.make(PhoneNumbers, employee_data=emp_info, phone_number=emp_phone)

        generated_data.append({
            "emp_name": emp_name,
            "emp_location": emp_location.unique_locations,
            "emp_phone": masked_phone
        })

    return JsonResponse({"Employee_details": generated_data})


def display_employee_info(request):
    """ function to display employee details """
    return render(request, 'emp_info.html')


def preview_page(request):
    """html page for preview of selected employees and creation of note and related document"""
    return render(request, "preview.html")


def report_page(request):
    """URL for report page"""
    return render(request, "report.html")


def menu_page(request):
    """ menu page to display all actions """
    return render(request, "menu.html")


def report_info(request):
    return render(request, "report_info.html")


def fetching_locations(request):
    location_data = Locations.get_unique_locations(request)
    unique_loc = [location.unique_locations for location in location_data]
    return JsonResponse({"unique_locations": unique_loc})


def employee_details(request):
    if request.method == "GET":
        location = request.GET.get("location", "All")
        page_size = int(request.GET.get('page_size', 10))

        employee_data = EmployeeInfo.get_employee_details(location)

        total = employee_data.count()
        employee_info = [
            {
                'emp_id': employee.id,
                'emp_name': employee.emp_name,
                'emp_location': employee.emp_location.unique_locations,
                'emp_phone': employee.emp_phone
            }
            for employee in employee_data
        ]
        return JsonResponse({
            "Employee_data": employee_info,
            "total": total,
            "page_size": page_size
        })


def add_campaign_data(request):
    if request.method == "POST":
        form = AddCampaignForm(request.POST, request.FILES)
        if not form.is_valid():
            return JsonResponse({"Error": form.errors}, status=400)

        note = form.cleaned_data['note_description']
        document = form.cleaned_data['document']
        schedule_date = form.cleaned_data['schedule_date']
        campaign_name = request.POST.get("campaign_name")
        phone_numbers_id = request.POST.get("phone_numbers_id")

        phone_numbers_id_list = phone_numbers_id.split(",")

        data = Campaign.create_campaign( campaign_name,note,document,schedule_date,phone_numbers_id_list)

        campaign_data = {
            "campaign_name": data.campaign_name,
            "schedule_date": data.schedule_date,
            "total_count_of_employees": data.total_count_of_employees,
            "note_description": data.note_description,
            "status": data.status,
            "document_url": data.document.url,

        }

        return JsonResponse(
            {
                "campaign": campaign_data
            }
        )


def fetch_campaign_info(request):
    if request.method == "GET":
        campaign_data = Campaign.campaign_info(request)

        campaign_report_list = [{
            "campaign_id": report.id,
            "campaign_name": report.campaign_name,
            "date_of_campaign": report.date_of_campaign,
            "total_count_of_employees": report.total_count_of_employees,
            "note_description": report.note_description,
            "document": str(report.document) if report.document else None,
            "status": report.status
        } for report in campaign_data]

        return JsonResponse({"campaign_report": campaign_report_list})

# def get_campaign_details(request):
#     if request.method == "GET":
#         campaign_id = request.GET.get('campaign_id')
#
#         campaign_info = CampaignDetails.objects.filter(campaign_id=campaign_id)
#
#         campaign_details_data = [
#             {
#                 "phone_number": campaign.phone_number,
#                 "masked_phone_numbers": campaign.masked_phone_numbers,
#                 "delivery_time": campaign.delivery_time,
#                 "note_status": campaign.note_status,
#             }
#             for campaign in campaign_info
#         ]
#
#         return JsonResponse({"campaign_details": campaign_details_data})
