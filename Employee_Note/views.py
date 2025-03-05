from django.http import JsonResponse
from django.shortcuts import render
from model_bakery import baker
from Employee_Note.forms import AddCampaignForm
from Employee_Note.models import EmployeeInfo, Locations, PhoneNumbers, Report
import random

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


def get_unique_locations(request):
    """ get all locations from the location table """
    locations = Locations.get_locations()
    unique_loc = [location.unique_locations for location in locations]
    return JsonResponse({"unique_locations": unique_loc})

def get_employee_details(request):

    if request.method == "GET":
        location = request.GET.get("location", "All")
        page = int(request.GET.get('page',1))
        page_size =int(request.GET.get('page_size',10))
        # print(64,type(page))
        # print(65,type(page_size))

        offset = (page - 1) * page_size
        limit = offset + 10
        employees = EmployeeInfo.objects.all()

        if location != "All":
            employees = employees.filter(emp_location__unique_locations=location)


        total = employees.count()
        # employees = employees[offset: offset + limit]
        employee_data = [
            {
                'emp_id': employee.id,
                'emp_name': employee.emp_name,
                'emp_location': employee.emp_location.unique_locations,
                'emp_phone': employee.emp_phone
            }
            for employee in employees
        ]
        return JsonResponse({
            "Employee_data": employee_data,
            "total":total,
            "page_size": page_size
        })


def preview_page(request):
    """html page for preview of selected employees and creation of note and related document"""
    return render(request,"preview.html")

def report_page(request):
    """URL for report page"""
    return render(request,"report.html")

def add_campaign_data(request):
    if request.method == "POST":
        form = AddCampaignForm(request.POST,request.FILES)
        if not form.is_valid():
            return JsonResponse({"Error":form.errors},status=400)

        note = form.cleaned_data['note_description']
        document = form.cleaned_data['document']
        campaign_name = request.POST.get("campaign_name")
        total_count_of_employees = request.POST.get("total_count_of_employees")


        new_campaign = Report.objects.create(
            campaign_name = campaign_name,
            total_count_of_employees = total_count_of_employees,
            note_description = note,
            document = document,
        )

        campaign_data = {
            "campaign_name": new_campaign.campaign_name,
            "total_count_of_employees": new_campaign.total_count_of_employees,
            "note_description": new_campaign.note_description,
            "status": new_campaign.status,
            "document_url": new_campaign.document.url
        }

        return JsonResponse(
            {
               "campaign": campaign_data
            }
        )

def campaign_report(request):
    """ Fetching Campaign report from report table"""
    if request.method == "GET":
        report_list = Report.objects.order_by("-id").first()
        campaign_report_list = {
                "campaign_id":report_list.id,
                "campaign_name":report_list.campaign_name,
                "date_of_campaign":report_list.date_of_campaign,
                "total_count_of_employees":report_list.total_count_of_employees,
                "note_description":report_list.note_description,
                "document":str(report_list.document) if report_list.document else None,
                "status":report_list.status
            }
        return JsonResponse({"campaign_report":campaign_report_list})