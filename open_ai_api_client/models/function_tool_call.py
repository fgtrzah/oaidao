from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.function_tool_call_type import FunctionToolCallType

if TYPE_CHECKING:
    from ..models.function_tool_call_function import FunctionToolCallFunction


T = TypeVar("T", bound="FunctionToolCall")


@_attrs_define
class FunctionToolCall:
    """
    Attributes:
        id (str): The ID of the tool call object.
        type (FunctionToolCallType): The type of tool call. This is always going to be `function` for this type of tool
            call.
        function (FunctionToolCallFunction): The definition of the function that was called.
    """

    id: str
    type: FunctionToolCallType
    function: "FunctionToolCallFunction"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        function = self.function.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "function": function,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.function_tool_call_function import FunctionToolCallFunction

        d = src_dict.copy()
        id = d.pop("id")

        type = FunctionToolCallType(d.pop("type"))

        function = FunctionToolCallFunction.from_dict(d.pop("function"))

        function_tool_call = cls(
            id=id,
            type=type,
            function=function,
        )

        function_tool_call.additional_properties = d
        return function_tool_call

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
