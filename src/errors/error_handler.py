from src.http_types.http_response import HttpResponse
from .http_conflict import HttpConflictError
from .http_not_found import HttpNotFoundError

def handle_error(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpNotFoundError, HttpConflictError)):
        return HttpResponse(
            status_code=error.status_code,
            body={"errors": [{
                "title": error.name,
                "detail": error.message
            }]}
        )

    return HttpResponse(
        body={"errors": [{
            "title": "ERROR",
            "detail": str(error)
        }]}
    )