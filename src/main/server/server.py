from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

from src.main.server.routes.event_routes import event_route_bp
from src.main.server.routes.attendees_routes import attendees_route_bp
from src.main.server.routes.check_ins_routes import check_ins_route_bp
app.register_blueprint(event_route_bp)
app.register_blueprint(attendees_route_bp)
app.register_blueprint(check_ins_route_bp)