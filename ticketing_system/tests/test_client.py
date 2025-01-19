SPECIAL_TICKET_ID = 1234

def test_client_get_ticket(
        test_client,
        add_special_ticket
):
  request = test_client.get(f"/tickets/{SPECIAL_TICKET_ID}")
  assert request.status_code == 200
  assert request.json() == {
      "id": SPECIAL_TICKET_ID,
      "show": "Special Show",
      "user": None,
      "price": 100.0
  }

def test_client_does_not_found_specific_ticket(
    test_client
):
  response = test_client.get("/tickets/1")
  assert response.status_code == 404
  assert response.json() == {"detail": "Ticket not found"}

def test_client_create_ticket(
    test_client,
):
    request = test_client.post(
        "/tickets",
        json={
            "price": 100.0,
            "show": "The Rolling Stones Concert",
            "user": "John Doe",
        },
    )
    assert request.status_code == 200
    assert request.json() == {"ticket_id": 1}

def test_client_update_ticket(
    test_client, add_special_ticket
):
    request = test_client.put(
        F"/tickets/{SPECIAL_TICKET_ID}", json={"price": 250.0}
    )
    assert request.status_code == 200
    assert request.json() == {
       "detail": "Ticket updated successfully",
       "ticket_id": SPECIAL_TICKET_ID
      }
    
def test_client_update_ticket_not_fund(
      test_client
):
  request = test_client.put(
      "/tickets/1", json={"price": 250.0}
  )
  assert request.status_code == 404
  assert request.json() == {
      "detail": "Ticket not found"
  }
    
def test_client_delete_ticket(
    test_client, add_special_ticket
):
    request = test_client.delete(f"/tickets/{SPECIAL_TICKET_ID}")
    assert request.status_code == 200
    assert request.json() == {
        "detail": "Ticket removed successfully",
        "ticket_id": SPECIAL_TICKET_ID
    }
    request = test_client.get(f"/tickets/{SPECIAL_TICKET_ID}")
    assert request.status_code == 404
    assert request.json() == {
        "detail": "Ticket not found"
    }

def test_client_delete_ticket_not_found(
    test_client
):
  request = test_client.delete("/tickets/1")
  assert request.status_code == 404
  assert request.json() == {
      "detail": "Ticket not found"
  }