from typing import TYPE_CHECKING, Any, Dict, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.modify_message_request_metadata import ModifyMessageRequestMetadata


T = TypeVar("T", bound="ModifyMessageRequest")


@_attrs_define
class ModifyMessageRequest:
    """
    Attributes:
        metadata (Union[Unset, None, ModifyMessageRequestMetadata]): Set of 16 key-value pairs that can be attached to
            an object. This can be useful for storing additional information about the object in a structured format. Keys
            can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    metadata: Union[Unset, None, "ModifyMessageRequestMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.modify_message_request_metadata import ModifyMessageRequestMetadata

        d = src_dict.copy()
        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, ModifyMessageRequestMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModifyMessageRequestMetadata.from_dict(_metadata)

        modify_message_request = cls(
            metadata=metadata,
        )

        return modify_message_request
