from django import forms


class AddCampaignForm(forms.Form):
    campaign_name = forms.CharField(max_length=32, required=True)
    note_description = forms.CharField(max_length=200, required=True)
    total_count = forms.IntegerField(required=True)
    document = forms.FileField(required=False)
    schedule_date = forms.DateField(required=True)

    def clean_note_description(self):
        note = self.cleaned_data.get("note_description")
        if not note:
            raise forms.ValidationError("note is required.")
        return note
