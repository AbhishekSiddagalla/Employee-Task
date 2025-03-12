import pytest

from django.core.files.uploadedfile import SimpleUploadedFile

from Employee_Note.models import EmployeeInfo,PhoneNumbers, Campaign, Locations

@pytest.fixture
def create_locations():
    location1 = Locations.objects.create(unique_locations="Location 1")

    return location1

@pytest.fixture
def create_employee_info(create_locations):
    record1 = EmployeeInfo.objects.create(emp_name="Emp_1",emp_location=create_locations,emp_phone="xxxxxx7890" )
    record2 = EmployeeInfo.objects.create(emp_name="Emp_2",emp_location=create_locations,emp_phone="xxxxxx3210" )
    record3 = EmployeeInfo.objects.create(emp_name="Emp_3",emp_location=create_locations,emp_phone="xxxxxx6783" )
    record4 = EmployeeInfo.objects.create(emp_name="Emp_4",emp_location=create_locations,emp_phone="xxxxxx9165" )
    record5 = EmployeeInfo.objects.create(emp_name="Emp_5",emp_location=create_locations,emp_phone="xxxxxx9654" )

    return record1

@pytest.fixture
def create_phone_numbers(create_employee_info):
    phone_number1 = PhoneNumbers.objects.create(employee_data=create_employee_info,phone_number="1234567890")
    phone_number2 = PhoneNumbers.objects.create(employee_data=create_employee_info,phone_number="9876543210")
    phone_number3 = PhoneNumbers.objects.create(employee_data=create_employee_info,phone_number="7987096783")
    phone_number4 = PhoneNumbers.objects.create(employee_data=create_employee_info,phone_number="7835479165")
    phone_number5 = PhoneNumbers.objects.create(employee_data=create_employee_info,phone_number="6300789654")
    return phone_number1.id,phone_number2.id,phone_number3.id,phone_number4.id,phone_number5.id

@pytest.mark.django_db
def test_campaign_model(create_phone_numbers):
    file_path = "C:\\Users\\AbhishekSiddagalla\\internship\\tasks\\Employee_Project\\test\\Guidelines.txt"

    with open(file_path, "rb") as fp:
        document = SimpleUploadedFile("Guidelines.txt", fp.read(), content_type="text/plain")

    campaign_name = "campaign 1"
    schedule_date = "2025-03-11"
    note = "Note Description 1"

    campaign = Campaign.create_campaign(
        campaign_name=campaign_name, note=note, document=document, schedule_date=schedule_date,
        phone_numbers_id_list=list(create_phone_numbers)
    )

    assert campaign.campaign_name == "campaign 1"
    assert campaign.schedule_date == "2025-03-11"
    assert campaign.total_count == 5
    assert campaign.note_description == "Note Description 1"
    assert campaign.document is not None
    assert campaign.status == "Ready"