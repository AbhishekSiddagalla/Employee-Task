import pytest

from Employee_Note.models import EmployeeInfo, Locations


@pytest.fixture
def create_locations():
    location1 = Locations.objects.create(unique_locations="Location 1")
    return location1


@pytest.fixture
def create_employees(create_locations):
    location1 = create_locations
    employee1 = EmployeeInfo.objects.create(emp_name="John Doe",
                                            emp_location=location1,
                                            emp_phone="1234567890")

    return employee1


@pytest.mark.django_db
def test_create_employee(create_employees):
    employee = create_employees
    expected_output = {
        "emp_name": "John Doe",
        "emp_location": "Location 1",
        "emp_phone": "1234567890"
    }

    assert employee.emp_name == expected_output["emp_name"]
    assert employee.emp_location.unique_locations == expected_output["emp_location"]
    assert employee.emp_phone == expected_output["emp_phone"]