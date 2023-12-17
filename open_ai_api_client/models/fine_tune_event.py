from typing import Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.fine_tune_event_object import FineTuneEventObject

T = TypeVar("T", bound="FineTuneEvent")


@_attrs_define
class FineTuneEvent:
    """Fine-tune event object

    Attributes:
        created_at (int):
        level (str):
        message (str):
        object_ (FineTuneEventObject):
    """

    created_at: int
    level: str
    message: str
    object_: FineTuneEventObject
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        created_at = self.created_at
        level = self.level
        message = self.message
        object_ = self.object_.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "created_at": created_at,
                "level": level,
                "message": message,
                "object": object_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        created_at = d.pop("created_at")

        level = d.pop("level")

        message = d.pop("message")

        object_ = FineTuneEventObject(d.pop("object"))

        fine_tune_event = cls(
            created_at=created_at,
            level=level,
            message=message,
            object_=object_,
        )

        fine_tune_event.additional_properties = d
        return fine_tune_event

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
