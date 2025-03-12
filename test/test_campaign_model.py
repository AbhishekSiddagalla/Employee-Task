import pytest

from django.core.files.uploadedfile import SimpleUploadedFile

from Employee_Note.models import EmployeeInfo,PhoneNumbers, Campaign, Locations, CampaignDetails

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

    return record1,record2,record3,record4,record5


@pytest.fixture
def create_phone_numbers(create_employee_info):
    phone_numbers = []

    for i, employee in enumerate(create_employee_info):
        phone_numbers.extend([
            PhoneNumbers.objects.create(employee_data=employee, phone_number=f"12345678{i + 1}0").id,
            PhoneNumbers.objects.create(employee_data=employee, phone_number=f"98765432{i + 1}0").id,
            PhoneNumbers.objects.create(employee_data=employee, phone_number=f"79870967{i + 1}0").id,
            PhoneNumbers.objects.create(employee_data=employee, phone_number=f"78354791{i + 1}0").id,
            PhoneNumbers.objects.create(employee_data=employee, phone_number=f"63007896{i + 1}0").id
        ])

    return phone_numbers


@pytest.mark.django_db
def test_campaign_model_with_valid_data(create_phone_numbers):
    file_path = "C:\\Users\\AbhishekSiddagalla\\internship\\tasks\\Employee_Project\\test\\Guidelines.txt"

    with open(file_path, "rb") as fp:
        document = SimpleUploadedFile("Guidelines.txt", fp.read(), content_type="text/plain")

    campaign_name = "campaign 1"
    schedule_date = "2025-03-11"
    note = "Note Description 1"

    campaign = Campaign.create_campaign(
        campaign_name=campaign_name, note=note, document=document, schedule_date=schedule_date,
        phone_numbers_id_list=create_phone_numbers
    )


    details_count = campaign.get_campaign_details().count()

    assert campaign.campaign_name == "campaign 1"
    assert campaign.schedule_date == "2025-03-11"
    assert campaign.total_count == 25
    assert details_count == 25
    assert campaign.note_description == "Note Description 1"
    assert campaign.document is not None
    assert campaign.status == "Ready"

@pytest.mark.django_db
def test_campaign_model_missing_campaign_name(create_phone_numbers):
    file_path = "C:\\Users\\AbhishekSiddagalla\\internship\\tasks\\Employee_Project\\test\\Guidelines.txt"

    with open(file_path, "rb") as fp:
        document = SimpleUploadedFile("Guidelines.txt", fp.read(), content_type="text/plain")

    schedule_date = "2025-03-11"
    note = "Note Description 1"

    with pytest.raises(ValueError):
        Campaign.create_campaign(
            campaign_name=None,
            note=note,
            document=document,
            schedule_date=schedule_date,
            phone_numbers_id_list=list(create_phone_numbers)
        )

@pytest.mark.django_db
def test_campaign_model_with_missing_note(create_phone_numbers):
    file_path = "C:\\Users\\AbhishekSiddagalla\\internship\\tasks\\Employee_Project\\test\\Guidelines.txt"

    with open(file_path, "rb") as fp:
        document = SimpleUploadedFile("Guidelines.txt", fp.read(), content_type="text/plain")

    schedule_date = "Invalid Date"

    with pytest.raises(ValueError):
        Campaign.create_campaign(
            campaign_name=None,
            note=None,
            document=document,
            schedule_date=schedule_date,
            phone_numbers_id_list=list(create_phone_numbers)
        )

@pytest.mark.django_db
def test_campaign_model_with_invalid_date(create_phone_numbers):
    file_path = "C:\\Users\\AbhishekSiddagalla\\internship\\tasks\\Employee_Project\\test\\Guidelines.txt"

    with open(file_path, "rb") as fp:
        document = SimpleUploadedFile("Guidelines.txt", fp.read(), content_type="text/plain")

    schedule_date = "Invalid Date"
    note = "Note Description 1"

    with pytest.raises(ValueError):
        Campaign.create_campaign(
            campaign_name=None,
            note=note,
            document=document,
            schedule_date=schedule_date,
            phone_numbers_id_list=list(create_phone_numbers)
        )

