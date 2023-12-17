from enum import Enum


class FineTuneObject(str, Enum):
    FINE_TUNE = "fine-tune"

    def __str__(self) -> str:
        return str(self.value)
