import pytest
from httpx import ASGITransport, AsyncClient
from protoapp.main import app
from protoapp.database import Item

@pytest.mark.asyncio
async def test_read_main():
  client=AsyncClient(
    transport=ASGITransport(app=app),
    base_url="http://test"
  )
  response=await client.get("/home")
  assert response.status_code==200
  assert response.json()=={
    "message": "Hello World"
  }

#more compact than above and easy to read using test_client configured in conftest.py
def test_read_main_client(test_client):
  response = test_client.get("/home")
  assert response.status_code == 200
  assert response.json() == {
    "message": "Hello World"
  }

@pytest.mark.integration
def test_client_can_add_read_the_item_from_database(
    test_client, test_db_session
):
  response = test_client.get("/item/1")
  assert response.status_code == 404

  response = test_client.post(
    "/item", json={"name":"ball", "color":"red"}
  )
  assert response.status_code == 201

  item_id = response.json()
  item = (
    test_db_session.query(Item)
    .filter(Item.id == item_id)
    .first()
  )

  assert item is not None
  response = test_client.get(f"/item/{item_id}")
  assert response.status_code == 200
  assert response.json() == {
    "name": "ball",
    "color": "red"
  }
