from enum import Enum


class EditChoicesItemFinishReason(str, Enum):
    LENGTH = "length"
    STOP = "stop"

    def __str__(self) -> str:
        return str(self.value)
