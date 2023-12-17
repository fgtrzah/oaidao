from enum import Enum


class CreateMessageRequestRole(str, Enum):
    USER = "user"

    def __str__(self) -> str:
        return str(self.value)
