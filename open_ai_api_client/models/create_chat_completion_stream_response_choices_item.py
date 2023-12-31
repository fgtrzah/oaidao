from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_chat_completion_stream_response_choices_item_finish_reason import (
    CreateChatCompletionStreamResponseChoicesItemFinishReason,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_stream_response_delta import ChatCompletionStreamResponseDelta
    from ..models.create_chat_completion_stream_response_choices_item_logprobs import (
        CreateChatCompletionStreamResponseChoicesItemLogprobs,
    )


T = TypeVar("T", bound="CreateChatCompletionStreamResponseChoicesItem")


@_attrs_define
class CreateChatCompletionStreamResponseChoicesItem:
    """
    Attributes:
        delta (ChatCompletionStreamResponseDelta): A chat completion delta generated by streamed model responses.
        index (int): The index of the choice in the list of choices.
        logprobs (Union[Unset, None, CreateChatCompletionStreamResponseChoicesItemLogprobs]): Log probability
            information for the choice.
        finish_reason (Optional[CreateChatCompletionStreamResponseChoicesItemFinishReason]): The reason the model
            stopped generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop
            sequence,
            `length` if the maximum number of tokens specified in the request was reached,
            `content_filter` if content was omitted due to a flag from our content filters,
            `tool_calls` if the model called a tool, or `function_call` (deprecated) if the model called a function.
    """

    delta: "ChatCompletionStreamResponseDelta"
    index: int
    finish_reason: Optional[CreateChatCompletionStreamResponseChoicesItemFinishReason]
    logprobs: Union[Unset, None, "CreateChatCompletionStreamResponseChoicesItemLogprobs"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        delta = self.delta.to_dict()

        index = self.index
        logprobs: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.logprobs, Unset):
            logprobs = self.logprobs.to_dict() if self.logprobs else None

        finish_reason = self.finish_reason.value if self.finish_reason else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "delta": delta,
                "index": index,
                "finish_reason": finish_reason,
            }
        )
        if logprobs is not UNSET:
            field_dict["logprobs"] = logprobs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_stream_response_delta import ChatCompletionStreamResponseDelta
        from ..models.create_chat_completion_stream_response_choices_item_logprobs import (
            CreateChatCompletionStreamResponseChoicesItemLogprobs,
        )

        d = src_dict.copy()
        delta = ChatCompletionStreamResponseDelta.from_dict(d.pop("delta"))

        index = d.pop("index")

        _logprobs = d.pop("logprobs", UNSET)
        logprobs: Union[Unset, None, CreateChatCompletionStreamResponseChoicesItemLogprobs]
        if _logprobs is None:
            logprobs = None
        elif isinstance(_logprobs, Unset):
            logprobs = UNSET
        else:
            logprobs = CreateChatCompletionStreamResponseChoicesItemLogprobs.from_dict(_logprobs)

        _finish_reason = d.pop("finish_reason")
        finish_reason: Optional[CreateChatCompletionStreamResponseChoicesItemFinishReason]
        if _finish_reason is None:
            finish_reason = None
        else:
            finish_reason = CreateChatCompletionStreamResponseChoicesItemFinishReason(_finish_reason)

        create_chat_completion_stream_response_choices_item = cls(
            delta=delta,
            index=index,
            logprobs=logprobs,
            finish_reason=finish_reason,
        )

        create_chat_completion_stream_response_choices_item.additional_properties = d
        return create_chat_completion_stream_response_choices_item

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
