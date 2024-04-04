import uuid
from src.models.repository.attendees_repository import AttendeesRepository
from src.models.repository.events_repository import EventsRepository
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest
from src.errors.http_not_found import HttpNotFoundError
from src.errors.http_conflict import HttpConflictError

class AttendeesHandler:
    
    def __init__(self) -> None:
        self.__attendees_repository = AttendeesRepository()
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        event_id = http_request.param["event_id"]

        event_attendee_count = self.__events_repository.count_event_attendees(event_id)
        if (
            event_attendee_count["attendees_amount"] and
            event_attendee_count["attendees_amount"] >= event_attendee_count["maximum_attendees"]
        ): raise HttpConflictError("Event is full")

        body["uuid"] = str(uuid.uuid4())
        body["event_id"] = event_id

        self.__attendees_repository.insert_attendee(body)

        return HttpResponse(
            status_code=201,
            body=None
        )

    def find_attendees_badge(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param["attendee_id"]
        badge = self.__attendees_repository.get_attendee_badge_by_id(attendee_id)
        if not badge: raise HttpNotFoundError("Attendee not found")

        return HttpResponse(
            status_code=200,
            body={
                "badge": {
                    "name": badge.name,
                    "email": badge.email,
                    "eventTitle": badge.title
                }
            }
        )

    def find_attendees_from_event(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        attendees = self.__attendees_repository.get_attendees_by_event_id(event_id)
        if not attendees: raise HttpNotFoundError("Attendees not found")

        attendees_list = []
        for attendee in attendees:
            attendees_list.append({
                "id": attendee.id,
                "name": attendee.name,
                "email": attendee.email,
                "checkedInAt": attendee.checkedInAt,
                "createdAt": attendee.createdAt
            })

        return HttpResponse(
            status_code=200,
            body={
                "attendees": attendees_list
            }
        )
