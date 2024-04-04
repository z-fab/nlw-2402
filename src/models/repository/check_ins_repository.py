from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import Check_ins
from sqlalchemy.exc import IntegrityError
from src.errors.http_conflict import HttpConflictError

class CheckinRepository:

    def insert_check_in(self, attendee_id: str):
        with db_connection_handler as database:
            try:
                check_in = Check_ins(
                    attendeeId = attendee_id
                )

                database.session.add(check_in)
                database.session.commit()

                return check_in
                
            except IntegrityError:
                raise HttpConflictError("Check in already inserted")
            except Exception as exception:
                database.session.rollback()
                raise exception