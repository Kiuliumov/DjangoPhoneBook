import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

from accounts.models import Account

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(
        username="john",
        email="john@example.com",
        password="StrongPassword123!",
        first_name="John",
        last_name="Doe",
    )

@pytest.fixture
def account(user):
    account = Account.objects.get(user=user)

    account.phone = "+123456789"
    account.gender = "M"
    account.bio = "Test account"
    account.save()

    return account

@pytest.fixture
def authenticated_client(user):
    client = APIClient()
    client.force_authenticate(user=user)
    return client
