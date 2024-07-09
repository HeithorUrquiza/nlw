import uuid
import pytest
from datetime import datetime, timedelta
from .trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

# Create a connection with the DB
db_connection_handler.connect()
trip_id = str(uuid.uuid4())

# Testing the creation of a trip
@pytest.mark.skip(reason="Interacao com o DB")
def test_create_trip():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trips_info = {
        "id": trip_id,
        "destination": "Osasco",
        "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
        "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        "owner_name": "Osvaldo",
        "owner_email": "osvaldo@email.com"
    }
    
    trips_repository.create_trip(trips_info)
    
# Testing find a trip by id
@pytest.mark.skip(reason="Interacao com o DB")
def test_find_trip_by_id():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trip = trips_repository.find_trip_by_id(trip_id)
    print(f"\n{trip}")

# Testing update status trip
@pytest.mark.skip(reason="Interacao com o DB")
def test_update_trip_status():
    conn = db_connection_handler.get_connection()
    trips_repository = TripsRepository(conn)
    
    trips_repository.update_trip_status(trip_id)