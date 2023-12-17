from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..models.create_message_request_role import CreateMessageRequestRole
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_message_request_metadata import CreateMessageRequestMetadata


T = TypeVar("T", bound="CreateMessageRequest")


@_attrs_define
class CreateMessageRequest:
    """
    Attributes:
        role (CreateMessageRequestRole): The role of the entity that is creating the message. Currently only `user` is
            supported.
        content (str): The content of the message.
        file_ids (Union[Unset, List[str]]): A list of [File](/docs/api-reference/files) IDs that the message should use.
            There can be a maximum of 10 files attached to a message. Useful for tools like `retrieval` and
            `code_interpreter` that can access and use files.
        metadata (Union[Unset, None, CreateMessageRequestMetadata]): Set of 16 key-value pairs that can be attached to
            an object. This can be useful for storing additional information about the object in a structured format. Keys
            can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    role: CreateMessageRequestRole
    content: str
    file_ids: Union[Unset, List[str]] = UNSET
    metadata: Union[Unset, None, "CreateMessageRequestMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        role = self.role.value

        content = self.content
        file_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "role": role,
                "content": content,
            }
        )
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.create_message_request_metadata import CreateMessageRequestMetadata

        d = src_dict.copy()
        role = CreateMessageRequestRole(d.pop("role"))

        content = d.pop("content")

        file_ids = cast(List[str], d.pop("file_ids", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CreateMessageRequestMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateMessageRequestMetadata.from_dict(_metadata)

        create_message_request = cls(
            role=role,
            content=content,
            file_ids=file_ids,
            metadata=metadata,
        )

        return create_message_request
