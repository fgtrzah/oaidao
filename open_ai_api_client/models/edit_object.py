from enum import Enum


class EditObject(str, Enum):
    EDIT = "edit"

    def __str__(self) -> str:
        return str(self.value)
