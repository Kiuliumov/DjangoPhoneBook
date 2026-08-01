import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_list_records(authenticated_client, phonebook_record):
    url = reverse("phonebook-records-list")

    response = authenticated_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]["name"] == "Alice Smith"


@pytest.mark.django_db
def test_create_record(authenticated_client):
    url = reverse("phonebook-records-list")

    response = authenticated_client.post(
        url,
        {
            "name": "Bob Smith",
            "number": "+987654321",
            "email": "bob@example.com",
            "profile_picture": "https://example.com/bob.jpg",
            "address": {
                "country": "UK",
                "state": "London",
                "city": "London",
                "line_1": "Baker Street",
                "line_2": "",
            },
        },
        format="json",
    )

    assert response.status_code == 201
    assert response.data["name"] == "Bob Smith"


@pytest.mark.django_db
def test_get_record(authenticated_client, phonebook_record):
    url = reverse(
        "phonebook-records-detail",
        kwargs={"pk": phonebook_record.id},
    )

    response = authenticated_client.get(url)

    assert response.status_code == 200
    assert response.data["email"] == "alice@example.com"


@pytest.mark.django_db
def test_update_record(authenticated_client, phonebook_record):
    url = reverse(
        "phonebook-records-detail",
        kwargs={"pk": phonebook_record.id},
    )

    response = authenticated_client.patch(
        url,
        {
            "name": "Alice Updated",
            "address": {
                "country": "USA",
                "city": "Boston",
                "line_1": "New Street",
                "line_2": "",
            },
        },
        format="json",
    )

    assert response.status_code == 200
    assert response.data["name"] == "Alice Updated"
    assert response.data["address"]["city"] == "Boston"


@pytest.mark.django_db
def test_delete_record(authenticated_client, phonebook_record):
    url = reverse(
        "phonebook-records-detail",
        kwargs={"pk": phonebook_record.id},
    )

    response = authenticated_client.delete(url)

    assert response.status_code == 204


@pytest.mark.django_db
def test_records_require_authentication(api_client):
    url = reverse("phonebook-records-list")

    response = api_client.get(url)

    assert response.status_code == 401
