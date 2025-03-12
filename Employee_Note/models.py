from django.db import models


class Locations(models.Model):
    unique_locations = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.unique_locations}"

    @classmethod
    def get_unique_locations(cls, request):
        """ get all locations from the location table """
        locations = cls.objects.all()
        return locations


class EmployeeInfo(models.Model):
    emp_name = models.CharField(max_length=32)
    emp_location = models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True)
    emp_phone = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f"{self.emp_name} - {self.emp_location} - {self.emp_phone}"

    @classmethod
    def get_employee_details(cls, location):
        """ fetching all employee details from EmployeeInfo table"""
        employees = cls.objects.all()

        if location != "All":
            employees = employees.filter(emp_location__unique_locations=location)

        return employees


class PhoneNumbers(models.Model):
    employee_data = models.ForeignKey(EmployeeInfo, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=10, default=None, unique=True)

    def __str__(self):
        return f"{self.phone_number}"


class Campaign(models.Model):
    campaign_name = models.CharField(max_length=32, default=None, unique=True)
    schedule_date = models.DateField(blank=True, null=True)
    total_count = models.PositiveIntegerField(blank=True, null=True)
    note_description = models.CharField(max_length=2048, default=None)
    document = models.FileField(
        upload_to='documents/',
        null=True,
        blank=True
    )
    status = models.CharField(max_length=16, default="Ready")

    def __str__(self):
        return self.campaign_name

    @classmethod
    def create_campaign(cls, campaign_name, note, document, schedule_date, phone_numbers_id_list):
        """ posting campaign data to report table """
        total_count = len(phone_numbers_id_list)

        if total_count < 1:
            raise Exception("Required Phone numbers")

        new_campaign = cls.objects.create(
            campaign_name=campaign_name,
            schedule_date=str(schedule_date),
            note_description=note,
            document=document,
            total_count=total_count
        )

        CampaignDetails.add_campaign_details(new_campaign, phone_numbers_id_list)

        return new_campaign

    @classmethod
    def campaign_info(cls, request):
        """ Fetching Campaign report from report table"""

        report_list = cls.objects.all()
        return report_list


class CampaignDetails(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True)
    employee_info = models.ForeignKey(EmployeeInfo, on_delete=models.SET_NULL, null=True)
    masked_phone_numbers = models.CharField(max_length=10, default=None)
    phone_number = models.CharField(max_length=10, default=None)
    delivery_time = models.DateTimeField(default=None, blank=True, null=True)
    note_status = models.CharField(max_length=10, default="ready")

    def __str__(self):
        return f"{self.campaign}- {self.masked_phone_numbers}"

    @classmethod
    def add_campaign_details(cls, new_campaign, list_phone_number):
        campaign_list = PhoneNumbers.objects.filter(employee_data_id__in=list_phone_number).values(
            "phone_number", "employee_data__emp_phone", "employee_data_id"
        )

        campaign_details_to_create = [
            cls(
                campaign=new_campaign,
                employee_info_id=campaign["employee_data_id"],
                masked_phone_numbers=campaign['employee_data__emp_phone'],
                phone_number=campaign['phone_number'],
                note_status="ready"
            )
            for campaign in campaign_list
        ]

        info = cls.objects.bulk_create(campaign_details_to_create)

        return info
