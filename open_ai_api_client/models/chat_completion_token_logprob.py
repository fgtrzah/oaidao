from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.chat_completion_token_logprob_top_logprobs_item import ChatCompletionTokenLogprobTopLogprobsItem


T = TypeVar("T", bound="ChatCompletionTokenLogprob")


@_attrs_define
class ChatCompletionTokenLogprob:
    """
    Attributes:
        token (str): The token.
        logprob (float): The log probability of this token.
        top_logprobs (List['ChatCompletionTokenLogprobTopLogprobsItem']): List of the most likely tokens and their log
            probability, at this token position. In rare cases, there may be fewer than the number of requested
            `top_logprobs` returned.
        bytes_ (Optional[List[int]]): A list of integers representing the UTF-8 bytes representation of the token.
            Useful in instances where characters are represented by multiple tokens and their byte representations must be
            combined to generate the correct text representation. Can be `null` if there is no bytes representation for the
            token.
    """

    token: str
    logprob: float
    top_logprobs: List["ChatCompletionTokenLogprobTopLogprobsItem"]
    bytes_: Optional[List[int]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        logprob = self.logprob
        top_logprobs = []
        for top_logprobs_item_data in self.top_logprobs:
            top_logprobs_item = top_logprobs_item_data.to_dict()

            top_logprobs.append(top_logprobs_item)

        if self.bytes_ is None:
            bytes_ = None
        else:
            bytes_ = self.bytes_

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "logprob": logprob,
                "top_logprobs": top_logprobs,
                "bytes": bytes_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.chat_completion_token_logprob_top_logprobs_item import ChatCompletionTokenLogprobTopLogprobsItem

        d = src_dict.copy()
        token = d.pop("token")

        logprob = d.pop("logprob")

        top_logprobs = []
        _top_logprobs = d.pop("top_logprobs")
        for top_logprobs_item_data in _top_logprobs:
            top_logprobs_item = ChatCompletionTokenLogprobTopLogprobsItem.from_dict(top_logprobs_item_data)

            top_logprobs.append(top_logprobs_item)

        bytes_ = cast(List[int], d.pop("bytes"))

        chat_completion_token_logprob = cls(
            token=token,
            logprob=logprob,
            top_logprobs=top_logprobs,
            bytes_=bytes_,
        )

        chat_completion_token_logprob.additional_properties = d
        return chat_completion_token_logprob

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
