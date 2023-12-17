from enum import Enum


class RetrievalToolType(str, Enum):
    RETRIEVAL = "retrieval"

    def __str__(self) -> str:
        return str(self.value)
