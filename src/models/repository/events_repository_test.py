import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_event():
    event = {
        "uuid": "meu-uuid-1234561",
        "title": "Event Title",
        "slug": "event-test2",
        "maximum_attendees": 100
    }

    event_repository = EventsRepository()
    response = event_repository.insert_event(event)

    print(response)

@pytest.mark.skip(reason="Não necessito")
def test_get_event_by_id():
    event_id = "meu-uuid-1234561"

    event_repository = EventsRepository()
    response = event_repository.get_event_by_id(event_id)

    print(response)