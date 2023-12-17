from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.retrieval_tool_call_type import RetrievalToolCallType

if TYPE_CHECKING:
    from ..models.retrieval_tool_call_retrieval import RetrievalToolCallRetrieval


T = TypeVar("T", bound="RetrievalToolCall")


@_attrs_define
class RetrievalToolCall:
    """
    Attributes:
        id (str): The ID of the tool call object.
        type (RetrievalToolCallType): The type of tool call. This is always going to be `retrieval` for this type of
            tool call.
        retrieval (RetrievalToolCallRetrieval): For now, this is always going to be an empty object.
    """

    id: str
    type: RetrievalToolCallType
    retrieval: "RetrievalToolCallRetrieval"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        type = self.type.value

        retrieval = self.retrieval.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type,
                "retrieval": retrieval,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.retrieval_tool_call_retrieval import RetrievalToolCallRetrieval

        d = src_dict.copy()
        id = d.pop("id")

        type = RetrievalToolCallType(d.pop("type"))

        retrieval = RetrievalToolCallRetrieval.from_dict(d.pop("retrieval"))

        retrieval_tool_call = cls(
            id=id,
            type=type,
            retrieval=retrieval,
        )

        retrieval_tool_call.additional_properties = d
        return retrieval_tool_call

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
