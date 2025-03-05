import pytest


@pytest.fixture
def populate_campaign_data():
    file_path = "C:\\Users\\AbhishekSiddagalla\internship\\tasks\Employee_Project\\test\Guidelines.txt"

    return {
        "campaign_name": "Guidelines for Employees",
        "total_count_of_employees": "100",
        "note_description": "All Employees must follow the Guidelines in the organization",
        "document": open(file_path,"rb")
    }


@pytest.mark.django_db
def test_campaign_details_with_valid_data(client,populate_campaign_data):
    """ testing with valid data"""
    response = client.post('/employee/api-add-campaign/',
                           populate_campaign_data,
                           format = "multipart"
                           )
    expected_output = {
        "campaign_name": "Guidelines for Employees",
        "total_count_of_employees": "100",
        "note_description": "All Employees must follow the Guidelines in the organization",
    }
    response_data = response.json()["campaign"]

    assert response_data["campaign_name"] == expected_output["campaign_name"]
    assert response_data["total_count_of_employees"] == expected_output["total_count_of_employees"]
    assert response_data["note_description"] == expected_output["note_description"]
    assert "document_url" in response_data
    assert response_data["document_url"] is not None

