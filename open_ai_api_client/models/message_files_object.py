from enum import Enum


class MessageFilesObject(str, Enum):
    THREAD_MESSAGE_FILE = "thread.message.file"

    def __str__(self) -> str:
        return str(self.value)
