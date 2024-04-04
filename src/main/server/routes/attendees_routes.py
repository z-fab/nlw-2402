from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.attendees_handler import AttendeesHandler

attendees_route_bp = Blueprint('attendees_route', __name__)

@attendees_route_bp.route('/events/<event_id>/register', methods=['POST'])
def create_attendees(event_id):
    http_resquest = HttpRequest(param={"event_id": event_id}, body = request.json)

    atendee_handler = AttendeesHandler()
    http_response = atendee_handler.register(http_resquest)
    return jsonify(http_response.body), http_response.status_code

@attendees_route_bp.route('/attendees/<attendee_id>/badge', methods=['GET'])
def get_attendees_badge(attendee_id):
    http_resquest = HttpRequest(param={"attendee_id": attendee_id})

    atendee_handler = AttendeesHandler()
    http_response = atendee_handler.find_attendees_badge(http_resquest)
    return jsonify(http_response.body), http_response.status_code

@attendees_route_bp.route('/events/<event_id>/attendees', methods=['GET'])
def attendees_badge(event_id):
    http_resquest = HttpRequest(param={"event_id": event_id})

    atendee_handler = AttendeesHandler()
    http_response = atendee_handler.find_attendees_from_event(http_resquest)
    return jsonify(http_response.body), http_response.status_code
