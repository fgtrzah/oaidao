from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.message_files_object import MessageFilesObject

T = TypeVar("T", bound="MessageFiles")


@_attrs_define
class MessageFiles:
    """A list of files attached to a `message`.

    Attributes:
        id (str): The identifier, which can be referenced in API endpoints.
        object_ (MessageFilesObject): The object type, which is always `thread.message.file`.
        created_at (int): The Unix timestamp (in seconds) for when the message file was created.
        message_id (str): The ID of the [message](/docs/api-reference/messages) that the [File](/docs/api-
            reference/files) is attached to.
    """

    id: str
    object_: MessageFilesObject
    created_at: int
    message_id: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_.value

        created_at = self.created_at
        message_id = self.message_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created_at": created_at,
                "message_id": message_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        object_ = MessageFilesObject(d.pop("object"))

        created_at = d.pop("created_at")

        message_id = d.pop("message_id")

        message_files = cls(
            id=id,
            object_=object_,
            created_at=created_at,
            message_id=message_id,
        )

        message_files.additional_properties = d
        return message_files

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
