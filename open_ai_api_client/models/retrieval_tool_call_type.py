from enum import Enum


class RetrievalToolCallType(str, Enum):
    RETRIEVAL = "retrieval"

    def __str__(self) -> str:
        return str(self.value)
