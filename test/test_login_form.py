# login form form testing

import pytest

from Employee_Note.forms import LoginWithCaptchaForm
# from captcha.models import CaptchaStore


# Helper to create a valid captcha challenge
# def generate_valid_captcha():
#     challenge = CaptchaStore.generate_key()
#     captcha = CaptchaStore.objects.get(hashkey=challenge)
#     return challenge, captcha.response
#
# @pytest.mark.django_db
# def test_loginform_with_valid_data():
#     hashkey,response = generate_valid_captcha()
#     form_data = {
#         "user_name": "test@gmail.com",
#         "password": "test@1234",
#         "captcha_text_0": hashkey,
#         "captcha_text_1": response,
#     }
#     form = LoginWithCaptchaForm(data=form_data)
#
#     assert form.is_valid()
