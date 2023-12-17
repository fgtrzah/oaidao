from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.submit_tool_outputs_run_request_tool_outputs_item import SubmitToolOutputsRunRequestToolOutputsItem


T = TypeVar("T", bound="SubmitToolOutputsRunRequest")


@_attrs_define
class SubmitToolOutputsRunRequest:
    """
    Attributes:
        tool_outputs (List['SubmitToolOutputsRunRequestToolOutputsItem']): A list of tools for which the outputs are
            being submitted.
    """

    tool_outputs: List["SubmitToolOutputsRunRequestToolOutputsItem"]

    def to_dict(self) -> Dict[str, Any]:
        tool_outputs = []
        for tool_outputs_item_data in self.tool_outputs:
            tool_outputs_item = tool_outputs_item_data.to_dict()

            tool_outputs.append(tool_outputs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "tool_outputs": tool_outputs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.submit_tool_outputs_run_request_tool_outputs_item import (
            SubmitToolOutputsRunRequestToolOutputsItem,
        )

        d = src_dict.copy()
        tool_outputs = []
        _tool_outputs = d.pop("tool_outputs")
        for tool_outputs_item_data in _tool_outputs:
            tool_outputs_item = SubmitToolOutputsRunRequestToolOutputsItem.from_dict(tool_outputs_item_data)

            tool_outputs.append(tool_outputs_item)

        submit_tool_outputs_run_request = cls(
            tool_outputs=tool_outputs,
        )

        return submit_tool_outputs_run_request
