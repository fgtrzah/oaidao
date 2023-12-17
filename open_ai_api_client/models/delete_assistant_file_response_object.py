from enum import Enum


class DeleteAssistantFileResponseObject(str, Enum):
    ASSISTANT_FILE_DELETED = "assistant.file.deleted"

    def __str__(self) -> str:
        return str(self.value)
