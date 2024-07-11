import uuid
from typing import Dict
from src.models.repositories.trips_repository import TripsRepository
from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.drivers.email_sender import send_email

class TripCreator:
    def __init__(self, trip_repository: TripsRepository, emails_repository: EmailsToInviteRepository) -> None:
        self.__trip_repository = trip_repository
        self.__emails_repository = emails_repository
        
    def create(self, body) -> Dict:
        try:
            emails = body.get("emails_to_invite")
            trip_id = str(uuid.uuid4())
            # Creating a new dict from body params
            trip_infos = { **body, "id": trip_id }
            
            self.__trip_repository.create_trip(trip_infos)
            
            if emails:
                # Register each email in the DB
                for email in emails:
                    self.__emails_repository.registry_email({
                        "email": email,
                        "trip_id": trip_id,
                        "id": str(uuid.uuid4())
                    })
                    
            send_email(
                [body["owner_email"]],
                f"Confirme sua viagem clicando no link ou copiando e colando-o em seu browser http://localhost:3000/trips/{trip_id}/confirm"
            )
                    
            return {
                "body": { "id": trip_id },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }
