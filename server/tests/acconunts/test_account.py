import pytest


@pytest.mark.django_db
def test_get_account(authenticated_client):
    response = authenticated_client.get("/accounts/me/")

    assert response.status_code == 200


@pytest.mark.django_db
def test_update_account(authenticated_client):
    response = authenticated_client.patch(
        "/accounts/me/",
        {
            "bio": "Updated bio",
            "phone": "+987654321",
        },
        format="json",
    )

    assert response.status_code == 200

    assert response.data["bio"] == "Updated bio"
    assert response.data["phone"] == "+987654321"


@pytest.mark.django_db
def test_account_requires_authentication(api_client):
    response = api_client.get("/accounts/me/")

    assert response.status_code == 401
