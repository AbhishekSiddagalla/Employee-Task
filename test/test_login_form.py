# login form form testing

import pytest

from Employee_Note.forms import LoginWithCaptchaForm
from captcha.models import CaptchaStore


#Helper to create a valid captcha challenge
def generate_valid_captcha():
    challenge = CaptchaStore.generate_key()
    captcha = CaptchaStore.objects.get(hashkey=challenge)
    return challenge, captcha.response

#testing with valid data
@pytest.mark.django_db
def test_loginform_with_valid_data():
    hashkey,response = generate_valid_captcha()
    form_data = {
        "user_name": "test@gmail.com",
        "password": "test@1234",
        "captcha_text_0": hashkey,
        "captcha_text_1": response,
    }
    form = LoginWithCaptchaForm(data=form_data)
    assert form.is_valid()
    # assert data["user_name"] == "test@gmail.com"
    # assert data["password"] == "test@1234"

@pytest.mark.django_db
def test_loginform_with_empty_data():
    form = LoginWithCaptchaForm(data={})

    assert not form.is_valid()
    assert "user_name" in form.errors
    assert "password" in form.errors
    assert "captcha_text" in form.errors



# testing with missing username field
@pytest.mark.django_db
def test_loginform_with_missing_username_field():
    hashkey,response = generate_valid_captcha()
    form_data = {
        "password": "test@1234",
        "captcha_text_0": hashkey,
        "captcha_text_1": response,
    }
    form = LoginWithCaptchaForm(data=form_data)

    assert not form.is_valid()
    assert "user_name" in form.errors

# testing with missing password field
@pytest.mark.django_db
def test_loginform_with_missing_password_field():
    hashkey,response = generate_valid_captcha()
    form_data = {
        "user_name": "test@gmail.com",
        "captcha_text_0": hashkey,
        "captcha_text_1": response,
    }
    form = LoginWithCaptchaForm(data=form_data)

    assert not form.is_valid()
    assert "password" in form.errors

@pytest.mark.django_db
def test_loginform_with_missing_captcha():
    form_data = {
        "user_name": "test@gmail.com",
        "password": "test@1234",
    }
    form = LoginWithCaptchaForm(data=form_data)

    assert not form.is_valid()
    assert "captcha_text" in form.errors


def test_loginform_with_invalid_username():
    hashkey,response = generate_valid_captcha()
    form_data = {
        "user_name": "test",
        "password": "test@1234",
        "captcha_text_0": hashkey,
        "captcha_text_1": response,
    }
    form = LoginWithCaptchaForm(data=form_data)

    assert "user_name" in form.errors