import pytest
from Employee_Note.models import Locations,EmployeeInfo

@pytest.fixture
def create_locations():
    location1 = Locations.objects.create(unique_locations="Location 1")
    location2 = Locations.objects.create(unique_locations="Location 2")
    return location1, location2

@pytest.fixture
def create_employees(create_locations):
    location1, location2 = create_locations
    employee1 = EmployeeInfo.objects.create(emp_name="John Doe", emp_location=location1, emp_phone="1234567890")
    employee2 = EmployeeInfo.objects.create(emp_name="Jane Doe", emp_location=location2, emp_phone="9876543210")
    employee3 = EmployeeInfo.objects.create(emp_name="Alice Smith", emp_location=location1, emp_phone="1112223333")
    return employee1, employee2, employee3

@pytest.mark.django_db
def test_get_emp_details_all(client,create_employees):
    """
    testing employee data with all locations
    """

    response = client.get('/employee/api-get-emp-details/', {'location': 'All'})
    assert len(response.json()['Employee_data']) == 3
    assert response.json()['Employee_data'][0]['emp_name'] == "John Doe"
    assert response.json()['Employee_data'][1]['emp_name'] == "Jane Doe"
    assert response.json()['Employee_data'][2]['emp_name'] == "Alice Smith"

@pytest.mark.django_db
def test_get_emp_details_location(client,create_employees):
    """
    testing employee data with location 1
    """

    response = client.get('/employee/api-get-emp-details/', {'location': 'Location 1'})
    assert len(response.json()['Employee_data']) == 2
    assert response.json()['Employee_data'][0]['emp_name'] == "John Doe"
    assert response.json()['Employee_data'][1]['emp_name'] == "Alice Smith"