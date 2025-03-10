from django.db import models

class Locations(models.Model):
    unique_locations = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.unique_locations}"

    @classmethod
    def get_locations(cls):
        return cls.objects.all()


class EmployeeInfo(models.Model):
    emp_name = models.CharField(max_length=32)
    emp_location = models.ForeignKey(Locations, on_delete=models.SET_NULL, null=True)
    emp_phone = models.CharField(max_length=10, default=None)

    def __str__(self):
        return f"{self.emp_name} - {self.emp_location} - {self.emp_phone}"


class PhoneNumbers(models.Model):
    employee_data = models.ForeignKey(EmployeeInfo, on_delete=models.SET_NULL, null=True)
    phone_number = models.CharField(max_length=10,default=None,unique=True)

    def __str__(self):
        return f"{self.phone_number}"

class Report(models.Model):
    campaign_name = models.CharField(max_length=32,default=None,unique=True)
    date_of_campaign = models.DateField(auto_now=True)
    total_count_of_employees = models.PositiveIntegerField()
    note_description = models.CharField(max_length=200,default=None)
    document = models.FileField(
        upload_to='documents/',
        null=True,
        blank=True
    )
    status = models.CharField(max_length=16, default="Ready")

    def __str__(self):
        return f"{self.campaign_name}"

class