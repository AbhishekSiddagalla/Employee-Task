import pytest
from django.core.files.uploadedfile import SimpleUploadedFile


@pytest.mark.django_db
def test_report_api_with_valid_data(client):
    """ Testing report model with valid data """
    file_path = "C:\\Users\\AbhishekSiddagalla\\internship\\tasks\\Employee_Project\\test\\Guidelines.txt"

    with open(file_path, "rb") as fp:
        document = SimpleUploadedFile("Guidelines.txt", fp.read(), content_type="text/plain")

    data = {
        'campaign_name': 'Test Campaign',
        'total_count_of_employees': 50,
        'note_description': 'Test note',
        'document': document,
        'status': 'Ready'
    }

    response = client.post('/employee/api-add-campaign/', data)
    response_data = response.json()['campaign']
    assert response_data['campaign_name'] == 'Test Campaign'
    assert response_data['total_count_of_employees'] == 50
    assert response_data['note_description'] == 'Test note'
    assert response_data['document'] == document
    assert response_data['status'] == 'Ready'


@pytest.mark.django_db
def test_report_api_with_missing_fields(client):
    """testing report model with missing fields"""
    file_path = "C:\\Users\\AbhishekSiddagalla\\internship\\tasks\\Employee_Project\\test\\Guidelines.txt"

    with open(file_path, "rb") as fp:
        document = SimpleUploadedFile("Guidelines.txt", fp.read(), content_type="text/plain")

    data = {
        'campaign_name': 'Test Campaign',
        'total_count_of_employees': '',
        'note_description': 'Test note',
        'document': document,
        'status': 'Ready'
    }
    expected_output = {'total_count_of_employees': ['This field is required.']}
    response = client.post('/employee/api-add-campaign/', data)
    response_data = response.json()  # ['campaign']
    print(response_data)
    assert response_data['Error'].get('total_count_of_employees') == expected_output.get('total_count_of_employees')
