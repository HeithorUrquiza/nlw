import uuid
from typing import Dict
from src.models.repositories.links_repository import LinksRepository

class LinkCreator:
    def __init__(self, links_repository: LinksRepository) -> None:
        self.__links_repository = links_repository
        
    def create(self, body, trip_id) -> Dict:
        try:
            link_id = str(uuid.uuid4())
            link_infos = { **body, "id": link_id, "trip_id": trip_id}
            
            self.__links_repository.registry_link(link_infos)
            
            return {
                "body": { "linkId": link_id },
                "status_code": 201
            }
        except Exception as exception:
            return {
                "body": { "error": "Bad Request", "message": str(exception)},
                "status_code": 400
            }