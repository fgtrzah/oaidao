from enum import Enum


class AssistantFilesObject(str, Enum):
    ASSISTANT_FILE = "assistant.file"

    def __str__(self) -> str:
        return str(self.value)
