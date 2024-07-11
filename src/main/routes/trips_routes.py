from flask import jsonify, Blueprint, request

# Importing controllers
from src.controllers.trip.trip_creator import TripCreator
from src.controllers.trip.trip_finder import TripFinder
from src.controllers.trip.trip_confirmer import TripConfirmer

from src.controllers.link.link_creator import LinkCreator
from src.controllers.link.link_finder import LinkFinder

from src.controllers.participant.participant_creator import ParticipantCreator
from src.controllers.participant.participant_finder import ParticipantFinder
from src.controllers.participant.participant_confirmer import ParticipantConfirmer

from src.controllers.activity.activity_creator import ActivityCreator
from src.controllers.activity.activity_finder import ActivityFinder

# Importing repositories
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.repositories.links_repository import LinksRepository
from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.participants_repository import ParticipantsRepository

# Importing connection manager
from src.models.settings.db_connection_handler import db_connection_handler


trips_routes_bp = Blueprint("trip_routes", __name__)

# Trips
@trips_routes_bp.route("/trips", methods=["POST"])
def create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    emails_repositoy = EmailsToInviteRepository(conn)
    controller = TripCreator(trips_repository, emails_repositoy)
    
    response = controller.create(request.json)
    
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>", methods=["GET"])
# The Flask framework is responsable to capture the id in the URL
def find_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripFinder(trips_repository)
    
    response = controller.find_trip_details(tripId)
    
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/confirm", methods=["GET"])
def confirm_trip(tripId):
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    controller = TripConfirmer(trips_repository)
    
    response = controller.confirm(tripId)
    
    return jsonify(response["body"]), response["status_code"]


# Links
@trips_routes_bp.route("/trips/<tripId>/links", methods=["POST"])
def create_trip_link(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkCreator(links_repository)
    
    response = controller.create(request.json, tripId)
    
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/links", methods=["GET"])
def find_trip_links(tripId):
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    controller = LinkFinder(links_repository)
    
    response = controller.find(tripId)
    
    return jsonify(response["body"]), response["status_code"]


# Participants
@trips_routes_bp.route("/trips/<tripId>/invites", methods=["POST"])
def registry_participant(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    emails_repository = EmailsToInviteRepository(conn)
    controller = ParticipantCreator(participants_repository, emails_repository)
    
    response = controller.create(request.json, tripId)
    
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/invites", methods=["GET"])
def get_trip_participants(tripId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantFinder(participants_repository)
    
    response = controller.find_participants_from_trip(tripId)
    
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<participantId>/confirm", methods=["GET"])
def confirm_participant(participantId):
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)
    controller = ParticipantConfirmer(participants_repository)
    
    response = controller.confirm(participantId)
    
    return jsonify(response["body"]), response["status_code"]


# Activities
@trips_routes_bp.route("/trips/<tripId>/activities", methods=["POST"])
def registry_activity(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityCreator(activities_repository)
    
    response = controller.create(request.json, tripId)
    
    return jsonify(response["body"]), response["status_code"]


@trips_routes_bp.route("/trips/<tripId>/activities", methods=["GET"])
def get_trip_activities(tripId):
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)
    controller = ActivityFinder(activities_repository)
    
    response = controller.find_activities_from_trip(tripId)
    
    return jsonify(response["body"]), response["status_code"]