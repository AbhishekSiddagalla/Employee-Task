# Generated by Django 5.1.6 on 2025-02-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('Employee_Note', '0009_rename_mobile_numbers_phonenumbers_employee_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign_name', models.CharField(default=None, max_length=32, unique=True)),
                ('date_of_campaign', models.DateField(auto_now=True)),
                ('total_count_of_employees', models.PositiveIntegerField()),
                ('note_description', models.CharField(default=None, max_length=200)),
                ('document', models.FileField(upload_to='documents/')),
            ],
        ),
    ]
