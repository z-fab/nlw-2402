import pytest
from src.models.settings.connection import db_connection_handler
from .attendees_repository import AttendeesRepository
from sqlalchemy.exc import IntegrityError, NoResultFound

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="Novo registro em banco de dados")
def test_insert_attendee():
    event_id = 'meu-uuid-1234561e'
    attendee = {
        "uuid": "meu-uuid-attendee3",
        "name": "Name Attendee",
        "email": "email@email.com",
        "event_id": event_id
    }

    attendee_repository = AttendeesRepository()
    response = attendee_repository.insert_attendee(attendee)

    print(response)

@pytest.mark.skip(reason="Sem necessidade")
def test_get_attendee_badge_by_id():
    attendee_id = "meu-uuid-attendee2a"

    attendee_repository = AttendeesRepository()
    response = attendee_repository.get_attendee_badge_by_id(attendee_id)

    print(response)