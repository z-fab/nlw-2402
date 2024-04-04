import uuid
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from src.errors.http_not_found import HttpNotFoundError

class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())

        self.__events_repository.insert_event(body)

        return HttpResponse(
            status_code=200,
            body={"eventId": body["uuid"]}
        )

    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]

        event = self.__events_repository.get_event_by_id(event_id)
        if not event: raise HttpNotFoundError("Event not found")

        event_attendee_count = self.__events_repository.count_event_attendees(event_id)

        return HttpResponse(
            status_code=200,
            body={
                "event": {
                    "id": event.id,
                    "title": event.title,
                    "details": event.details,
                    "slug": event.slug,
                    "maximum_attendees": event.maximum_attendees,
                    "attendees_amount": event_attendee_count["attendees_amount"]
                }
            }
        )