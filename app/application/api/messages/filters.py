from infra.repositories.filters.messages import GetMessagesFilters
from pydantic import BaseModel


class GetMessagesFilters(BaseModel):
    limit: int = 10
    offset: int = 0

    def to_infta(self):
        return GetMessagesFilters(limit=self.limit, offset=self.offset)
