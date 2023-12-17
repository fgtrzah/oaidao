from enum import Enum


class CreateFileRequestPurpose(str, Enum):
    ASSISTANTS = "assistants"
    FINE_TUNE = "fine-tune"

    def __str__(self) -> str:
        return str(self.value)
