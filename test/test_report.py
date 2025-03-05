import pytest
from Employee_Note.models import Report
from datetime import date
@pytest.fixture
def generate_campaigns():
    file_path = "C:\\Users\\AbhishekSiddagalla\internship\\tasks\Employee_Project\\test\Guidelines.txt"
    with open(file_path,"rb") as fp:
        document = fp.read()
    campaign_1 = Report.objects.create(
        campaign_name = "change in shift timings",
        total_count_of_employees = 20,
        note_description = "shift timings are changing from today onwards",
        document = str(document),
        date_of_campaign = date.today()
    )
    return campaign_1

@pytest.mark.django_db
def test_campaign_report(client,generate_campaigns):
    campaign_data = {
        'campaign_name': generate_campaigns.campaign_name,
        'total_count_of_employees': generate_campaigns.total_count_of_employees,
        'note_description': generate_campaigns.note_description,
        # 'document': generate_campaigns.document,
        'date_of_campaign': str(generate_campaigns.date_of_campaign)
    }
    response = client.get(
        '/employee/api-campaign-report/',
        data=campaign_data,
        format = "multipart"
    )
    file_path = "C:\\Users\\AbhishekSiddagalla\internship\\tasks\Employee_Project\\test\Guidelines.txt"
    with open(file_path,"rb") as fp:
        document = fp.read()
    expected_output = {
        "campaign_name" : "change in shift timings",
        "total_count_of_employees" : 20,
        "note_description" : "shift timings are changing from today onwards",
        "document" : str(document),
        "date_of_campaign" : str(date.today())
    }
    response_data = response.json()["campaign_report"]
    print(response_data)
    assert response_data["campaign_name"] == expected_output["campaign_name"]
    assert response_data["total_count_of_employees"] == expected_output["total_count_of_employees"]
    assert response_data["note_description"] == expected_output["note_description"]
    assert response_data["document"] is not None
    assert response_data["date_of_campaign"] == expected_output["date_of_campaign"]

