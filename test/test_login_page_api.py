import pytest

from django.test import Client

from captcha.models import CaptchaStore

from Employee_Note.views import login_page


#Helper to create a valid captcha challenge
@pytest.fixture
def generate_valid_captcha():
    challenge = CaptchaStore.generate_key()
    captcha = CaptchaStore.objects.get(hashkey=challenge)
    return challenge, captcha.response


#testing login page with valid data
@pytest.mark.django_db
def test_login_page_with_valid_data(generate_valid_captcha):
    client = Client()
    hashkey, captcha_response = generate_valid_captcha
    user_data = {
        "user_name" : "test@gmail.com",
        "password" : "Test@123",
        "captcha_text_0" : hashkey,
        "captcha_text_1" : captcha_response
    }

    response = client.post("/login/", data=user_data)

    print(response.json())
    assert response.status_code == 200
    assert response.json()["success"] == True

# testing login page with invalid username
@pytest.mark.django_db
def test_login_page_with_invalid_username(generate_valid_captcha):
    client = Client()
    hashkey, captcha_response = generate_valid_captcha
    user_data = {
        "user_name": "test",
        "password": "Test@123",
        "captcha_text_0": hashkey,
        "captcha_text_1": captcha_response
    }

    response = client.post("/login/", data=user_data)

    print(response.json())
    assert response.status_code == 200
    assert response.json()["success"] == False


@pytest.mark.django_db
def test_login_page_with_missing_field(generate_valid_captcha):
    client = Client()
    hashkey, captcha_response = generate_valid_captcha
    user_data = {
        "user_name": "test@gmail.com",
        "captcha_text_0": hashkey,
        "captcha_text_1": captcha_response
    }

    response = client.post("/login/", data=user_data)

    print(response.json())
    assert response.status_code == 200
    assert response.json()["success"] == False

@pytest.mark.django_db
def test_login_page_with_empty_data():
    client = Client()
    response = client.post("/login/", data={})

    print(response.json())
    assert response.status_code == 200
    assert response.json()["success"] == False
