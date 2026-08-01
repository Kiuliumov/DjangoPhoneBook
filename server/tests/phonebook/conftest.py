import pytest
from django.contrib.auth import get_user_model

from phonebook.models import Address, PhoneBookRecord

User = get_user_model()


@pytest.fixture
def address():
    return Address.objects.create(
        country="USA",
        state="NY",
        city="New York",
        line_1="5th Avenue",
        line_2="Apartment 10",
    )


@pytest.fixture
def phonebook_record(user, address):
    return PhoneBookRecord.objects.create(
        user=user,
        address=address,
        name="Alice Smith",
        number="+123456789",
        email="alice@example.com",
        profile_picture="https://example.com/avatar.jpg",
    )
