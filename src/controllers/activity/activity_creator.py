import uuid
from typing import Dict
from src.models.repositories.activities_repository import ActivitiesRepository

class ActivityCreator:
    def __init__(self, activity_repository: ActivitiesRepository) -> None:
        self.__activity_repository = activity_repository
        
    def create(self, body: Dict, trip_id: str) -> Dict:
        try:
            id = str(uuid.uuid4())
            activity_infos = {
                "id": id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }
            self.__activity_repository.registry_activity(activity_infos)
            return {
                "body": { "activity_id": id},
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }