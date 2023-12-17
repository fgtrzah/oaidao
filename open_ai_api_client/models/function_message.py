from typing import Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.function_message_role import FunctionMessageRole

T = TypeVar("T", bound="FunctionMessage")


@_attrs_define
class FunctionMessage:
    """
    Attributes:
        role (FunctionMessageRole): The role of the messages author, in this case `function`.
        name (str): The name of the function to call.
        content (Optional[str]): The contents of the function message.
    """

    role: FunctionMessageRole
    name: str
    content: Optional[str]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        name = self.name
        content = self.content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
                "name": name,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        role = FunctionMessageRole(d.pop("role"))

        name = d.pop("name")

        content = d.pop("content")

        function_message = cls(
            role=role,
            name=name,
            content=content,
        )

        function_message.additional_properties = d
        return function_message

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
