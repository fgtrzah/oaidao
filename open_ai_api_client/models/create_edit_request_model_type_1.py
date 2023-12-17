from enum import Enum


class CreateEditRequestModelType1(str, Enum):
    CODE_DAVINCI_EDIT_001 = "code-davinci-edit-001"
    TEXT_DAVINCI_EDIT_001 = "text-davinci-edit-001"

    def __str__(self) -> str:
        return str(self.value)
