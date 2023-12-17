from typing import Any, Dict, Type, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="CreateAssistantFileRequest")


@_attrs_define
class CreateAssistantFileRequest:
    """
    Attributes:
        file_id (str): A [File](/docs/api-reference/files) ID (with `purpose="assistants"`) that the assistant should
            use. Useful for tools like `retrieval` and `code_interpreter` that can access files.
    """

    file_id: str

    def to_dict(self) -> Dict[str, Any]:
        file_id = self.file_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "file_id": file_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        file_id = d.pop("file_id")

        create_assistant_file_request = cls(
            file_id=file_id,
        )

        return create_assistant_file_request
