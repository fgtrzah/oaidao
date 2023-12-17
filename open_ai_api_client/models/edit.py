from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.edit_object import EditObject

if TYPE_CHECKING:
    from ..models.completion_usage import CompletionUsage
    from ..models.edit_choices_item import EditChoicesItem


T = TypeVar("T", bound="Edit")


@_attrs_define
class Edit:
    """
    Attributes:
        choices (List['EditChoicesItem']): A list of edit choices. Can be more than one if `n` is greater than 1.
        object_ (EditObject): The object type, which is always `edit`.
        created (int): The Unix timestamp (in seconds) of when the edit was created.
        usage (CompletionUsage): Usage statistics for the completion request.
    """

    choices: List["EditChoicesItem"]
    object_: EditObject
    created: int
    usage: "CompletionUsage"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()

            choices.append(choices_item)

        object_ = self.object_.value

        created = self.created
        usage = self.usage.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "choices": choices,
                "object": object_,
                "created": created,
                "usage": usage,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.completion_usage import CompletionUsage
        from ..models.edit_choices_item import EditChoicesItem

        d = src_dict.copy()
        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = EditChoicesItem.from_dict(choices_item_data)

            choices.append(choices_item)

        object_ = EditObject(d.pop("object"))

        created = d.pop("created")

        usage = CompletionUsage.from_dict(d.pop("usage"))

        edit = cls(
            choices=choices,
            object_=object_,
            created=created,
            usage=usage,
        )

        edit.additional_properties = d
        return edit

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
