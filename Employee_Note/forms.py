from django import forms

class AddCampaignForm(forms.Form):
    campaign_name = forms.CharField(max_length=32, required=True)
    note_description = forms.CharField(max_length=200, required=True)
    total_count_of_employees = forms.IntegerField(required=True)
    document = forms.FileField(required=True)