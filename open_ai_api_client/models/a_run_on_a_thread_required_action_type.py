from enum import Enum


class ARunOnAThreadRequiredActionType(str, Enum):
    SUBMIT_TOOL_OUTPUTS = "submit_tool_outputs"

    def __str__(self) -> str:
        return str(self.value)
