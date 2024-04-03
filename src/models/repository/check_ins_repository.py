from src.models.settings.connection import db_connection_handler
from src.models.entities.check_ins import Check_ins
from sqlalchemy.exc import IntegrityError

class CheckinRepository:

    def insert_check_in(self, attendee_id: String):
        with db_connection_handler as database:
            try:
                check_in = Check_ins(
                    attendee_id = attendee_id
                )

                database.session.add(attendee)
                database.session.commit()

                return attendeeInfo
                
            except IntegrityError:
                raise Exception("Check in already inserted")
            except Exception as exception:
                database.session.rollback()
                raise exception