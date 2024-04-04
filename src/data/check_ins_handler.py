import uuid
from src.models.repository.check_ins_repository import CheckinRepository
from src.http_types.http_response import HttpResponse
from src.http_types.http_request import HttpRequest

class CheckInHandler:
    
    def __init__(self) -> None:
        self.__check_ins_repository = CheckinRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        attendee_id = http_request.param["attendee_id"]
        self.__check_ins_repository.insert_check_in(attendee_id)

        return HttpResponse(
            status_code=201,
            body=None
        )
