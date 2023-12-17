from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_completion_response_choices_item_finish_reason import (
    CreateCompletionResponseChoicesItemFinishReason,
)

if TYPE_CHECKING:
    from ..models.create_completion_response_choices_item_logprobs import CreateCompletionResponseChoicesItemLogprobs


T = TypeVar("T", bound="CreateCompletionResponseChoicesItem")


@_attrs_define
class CreateCompletionResponseChoicesItem:
    """
    Attributes:
        finish_reason (CreateCompletionResponseChoicesItemFinishReason): The reason the model stopped generating tokens.
            This will be `stop` if the model hit a natural stop point or a provided stop sequence,
            `length` if the maximum number of tokens specified in the request was reached,
            or `content_filter` if content was omitted due to a flag from our content filters.
        index (int):
        text (str):
        logprobs (Optional[CreateCompletionResponseChoicesItemLogprobs]):
    """

    finish_reason: CreateCompletionResponseChoicesItemFinishReason
    index: int
    text: str
    logprobs: Optional["CreateCompletionResponseChoicesItemLogprobs"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        finish_reason = self.finish_reason.value

        index = self.index
        text = self.text
        logprobs = self.logprobs.to_dict() if self.logprobs else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "finish_reason": finish_reason,
                "index": index,
                "text": text,
                "logprobs": logprobs,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_completion_response_choices_item_logprobs import (
            CreateCompletionResponseChoicesItemLogprobs,
        )

        d = src_dict.copy()
        finish_reason = CreateCompletionResponseChoicesItemFinishReason(d.pop("finish_reason"))

        index = d.pop("index")

        text = d.pop("text")

        _logprobs = d.pop("logprobs")
        logprobs: Optional[CreateCompletionResponseChoicesItemLogprobs]
        if _logprobs is None:
            logprobs = None
        else:
            logprobs = CreateCompletionResponseChoicesItemLogprobs.from_dict(_logprobs)

        create_completion_response_choices_item = cls(
            finish_reason=finish_reason,
            index=index,
            text=text,
            logprobs=logprobs,
        )

        create_completion_response_choices_item.additional_properties = d
        return create_completion_response_choices_item

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
