from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.thread_object import ThreadObject

if TYPE_CHECKING:
    from ..models.thread_metadata import ThreadMetadata


T = TypeVar("T", bound="Thread")


@_attrs_define
class Thread:
    """Represents a thread that contains [messages](/docs/api-reference/messages).

    Attributes:
        id (str): The identifier, which can be referenced in API endpoints.
        object_ (ThreadObject): The object type, which is always `thread`.
        created_at (int): The Unix timestamp (in seconds) for when the thread was created.
        metadata (Optional[ThreadMetadata]): Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured format. Keys can be a maximum of 64
            characters long and values can be a maxium of 512 characters long.
    """

    id: str
    object_: ThreadObject
    created_at: int
    metadata: Optional["ThreadMetadata"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        object_ = self.object_.value

        created_at = self.created_at
        metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created_at": created_at,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.thread_metadata import ThreadMetadata

        d = src_dict.copy()
        id = d.pop("id")

        object_ = ThreadObject(d.pop("object"))

        created_at = d.pop("created_at")

        _metadata = d.pop("metadata")
        metadata: Optional[ThreadMetadata]
        if _metadata is None:
            metadata = None
        else:
            metadata = ThreadMetadata.from_dict(_metadata)

        thread = cls(
            id=id,
            object_=object_,
            created_at=created_at,
            metadata=metadata,
        )

        thread.additional_properties = d
        return thread

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
