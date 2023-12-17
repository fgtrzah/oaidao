from enum import Enum


class FineTuneEventObject(str, Enum):
    FINE_TUNE_EVENT = "fine-tune-event"

    def __str__(self) -> str:
        return str(self.value)
