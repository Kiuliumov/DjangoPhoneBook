import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


@pytest.mark.django_db
def test_register(api_client):
    url = reverse("users-register")

    response = api_client.post(
        url,
        {
            "username": "alice",
            "email": "alice@example.com",
            "password": "StrongPassword123!",
            "first_name": "Alice",
            "last_name": "Smith",
            "account": {
                "phone": "+123456789",
                "gender": "F",
                "bio": "Hello",
            },
        },
        format="json",
    )

    assert response.status_code == 201
    assert User.objects.filter(username="alice").exists()


@pytest.mark.django_db
def test_login(api_client, user):
    url = reverse("users-login")

    response = api_client.post(
        url,
        {
            "username": user.username,
            "password": "StrongPassword123!",
        },
        format="json",
    )

    assert response.status_code == 200

    assert "access" in response.data
    assert "refresh" in response.data
