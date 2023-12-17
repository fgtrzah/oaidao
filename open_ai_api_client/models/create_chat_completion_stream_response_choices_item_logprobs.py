from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_completion_token_logprob import ChatCompletionTokenLogprob


T = TypeVar("T", bound="CreateChatCompletionStreamResponseChoicesItemLogprobs")


@_attrs_define
class CreateChatCompletionStreamResponseChoicesItemLogprobs:
    """Log probability information for the choice.

    Attributes:
        content (Optional[List['ChatCompletionTokenLogprob']]): A list of message content tokens with log probability
            information.
    """

    content: Optional[List["ChatCompletionTokenLogprob"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        if self.content is None:
            content = None
        else:
            content = []
            for content_item_data in self.content:
                content_item = content_item_data.to_dict()

                content.append(content_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_token_logprob import ChatCompletionTokenLogprob

        d = src_dict.copy()
        content = []
        _content = d.pop("content")
        for content_item_data in _content or []:
            content_item = ChatCompletionTokenLogprob.from_dict(content_item_data)

            content.append(content_item)

        create_chat_completion_stream_response_choices_item_logprobs = cls(
            content=content,
        )

        create_chat_completion_stream_response_choices_item_logprobs.additional_properties = d
        return create_chat_completion_stream_response_choices_item_logprobs

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
