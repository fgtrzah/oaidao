from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_chat_completion_function_response_choices_item_finish_reason import (
    CreateChatCompletionFunctionResponseChoicesItemFinishReason,
)

if TYPE_CHECKING:
    from ..models.chat_completion_response_message import ChatCompletionResponseMessage


T = TypeVar("T", bound="CreateChatCompletionFunctionResponseChoicesItem")


@_attrs_define
class CreateChatCompletionFunctionResponseChoicesItem:
    """
    Attributes:
        finish_reason (CreateChatCompletionFunctionResponseChoicesItemFinishReason): The reason the model stopped
            generating tokens. This will be `stop` if the model hit a natural stop point or a provided stop sequence,
            `length` if the maximum number of tokens specified in the request was reached, `content_filter` if content was
            omitted due to a flag from our content filters, or `function_call` if the model called a function.
        index (int): The index of the choice in the list of choices.
        message (ChatCompletionResponseMessage): A chat completion message generated by the model.
    """

    finish_reason: CreateChatCompletionFunctionResponseChoicesItemFinishReason
    index: int
    message: "ChatCompletionResponseMessage"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        finish_reason = self.finish_reason.value

        index = self.index
        message = self.message.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "finish_reason": finish_reason,
                "index": index,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_response_message import ChatCompletionResponseMessage

        d = src_dict.copy()
        finish_reason = CreateChatCompletionFunctionResponseChoicesItemFinishReason(d.pop("finish_reason"))

        index = d.pop("index")

        message = ChatCompletionResponseMessage.from_dict(d.pop("message"))

        create_chat_completion_function_response_choices_item = cls(
            finish_reason=finish_reason,
            index=index,
            message=message,
        )

        create_chat_completion_function_response_choices_item.additional_properties = d
        return create_chat_completion_function_response_choices_item

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
