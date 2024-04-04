from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.data.check_ins_handler import CheckInHandler

check_ins_route_bp = Blueprint('check_ins_router', __name__)

@check_ins_route_bp.route('/attendees/<attendee_id>/check-in', methods=['POST'])
def create_check_in(attendee_id):
    http_resquest = HttpRequest(param={"attendee_id": attendee_id})

    check_in_handler = CheckInHandler()
    http_response = check_in_handler.register(http_resquest)
    return jsonify(http_response.body), http_response.status_code