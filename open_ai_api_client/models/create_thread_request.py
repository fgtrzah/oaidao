from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_message_request import CreateMessageRequest
    from ..models.create_thread_request_metadata import CreateThreadRequestMetadata


T = TypeVar("T", bound="CreateThreadRequest")


@_attrs_define
class CreateThreadRequest:
    """
    Attributes:
        messages (Union[Unset, List['CreateMessageRequest']]): A list of [messages](/docs/api-reference/messages) to
            start the thread with.
        metadata (Union[Unset, None, CreateThreadRequestMetadata]): Set of 16 key-value pairs that can be attached to an
            object. This can be useful for storing additional information about the object in a structured format. Keys can
            be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    messages: Union[Unset, List["CreateMessageRequest"]] = UNSET
    metadata: Union[Unset, None, "CreateThreadRequestMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        messages: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.messages, Unset):
            messages = []
            for messages_item_data in self.messages:
                messages_item = messages_item_data.to_dict()

                messages.append(messages_item)

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if messages is not UNSET:
            field_dict["messages"] = messages
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_message_request import CreateMessageRequest
        from ..models.create_thread_request_metadata import CreateThreadRequestMetadata

        d = src_dict.copy()
        messages = []
        _messages = d.pop("messages", UNSET)
        for messages_item_data in _messages or []:
            messages_item = CreateMessageRequest.from_dict(messages_item_data)

            messages.append(messages_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CreateThreadRequestMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateThreadRequestMetadata.from_dict(_metadata)

        create_thread_request = cls(
            messages=messages,
            metadata=metadata,
        )

        return create_thread_request
