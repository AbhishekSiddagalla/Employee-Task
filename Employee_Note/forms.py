from django import forms

from captcha.fields import CaptchaField

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

class LoginWithCaptchaForm(forms.Form):
    user_name = forms.EmailField(required=True)
    password = forms.CharField(max_length=15, required=True)
    captcha_text = CaptchaField()

    def clean_user_name(self):
        username = self.cleaned_data.get("user_name")

        if not username:
            raise forms.ValidationError("username is required.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")

        if not password:
            raise forms.ValidationError("password is required.")
        return password
