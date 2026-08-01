import pytest
from django.contrib.auth import get_user_model

from accounts.models import Account

User = get_user_model()


@pytest.fixture
def account(user):
    account = Account.objects.get(user=user)

    account.phone = "+123456789"
    account.gender = "M"
    account.bio = "Test account"
    account.save()

    return account
