from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.the_message_object_object import TheMessageObjectObject
from ..models.the_message_object_role import TheMessageObjectRole

if TYPE_CHECKING:
    from ..models.image_file import ImageFile
    from ..models.text import Text
    from ..models.the_message_object_metadata import TheMessageObjectMetadata


T = TypeVar("T", bound="TheMessageObject")


@_attrs_define
class TheMessageObject:
    """Represents a message within a [thread](/docs/api-reference/threads).

    Attributes:
        id (str): The identifier, which can be referenced in API endpoints.
        object_ (TheMessageObjectObject): The object type, which is always `thread.message`.
        created_at (int): The Unix timestamp (in seconds) for when the message was created.
        thread_id (str): The [thread](/docs/api-reference/threads) ID that this message belongs to.
        role (TheMessageObjectRole): The entity that produced the message. One of `user` or `assistant`.
        content (List[Union['ImageFile', 'Text']]): The content of the message in array of text and/or images.
        file_ids (List[str]): A list of [file](/docs/api-reference/files) IDs that the assistant should use. Useful for
            tools like retrieval and code_interpreter that can access files. A maximum of 10 files can be attached to a
            message.
        assistant_id (Optional[str]): If applicable, the ID of the [assistant](/docs/api-reference/assistants) that
            authored this message.
        run_id (Optional[str]): If applicable, the ID of the [run](/docs/api-reference/runs) associated with the
            authoring of this message.
        metadata (Optional[TheMessageObjectMetadata]): Set of 16 key-value pairs that can be attached to an object. This
            can be useful for storing additional information about the object in a structured format. Keys can be a maximum
            of 64 characters long and values can be a maxium of 512 characters long.
    """

    id: str
    object_: TheMessageObjectObject
    created_at: int
    thread_id: str
    role: TheMessageObjectRole
    content: List[Union["ImageFile", "Text"]]
    file_ids: List[str]
    assistant_id: Optional[str]
    run_id: Optional[str]
    metadata: Optional["TheMessageObjectMetadata"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.image_file import ImageFile

        id = self.id
        object_ = self.object_.value

        created_at = self.created_at
        thread_id = self.thread_id
        role = self.role.value

        content = []
        for content_item_data in self.content:
            content_item: Dict[str, Any]

            if isinstance(content_item_data, ImageFile):
                content_item = content_item_data.to_dict()

            else:
                content_item = content_item_data.to_dict()

            content.append(content_item)

        file_ids = self.file_ids

        assistant_id = self.assistant_id
        run_id = self.run_id
        metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created_at": created_at,
                "thread_id": thread_id,
                "role": role,
                "content": content,
                "file_ids": file_ids,
                "assistant_id": assistant_id,
                "run_id": run_id,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.image_file import ImageFile
        from ..models.text import Text
        from ..models.the_message_object_metadata import TheMessageObjectMetadata

        d = src_dict.copy()
        id = d.pop("id")

        object_ = TheMessageObjectObject(d.pop("object"))

        created_at = d.pop("created_at")

        thread_id = d.pop("thread_id")

        role = TheMessageObjectRole(d.pop("role"))

        content = []
        _content = d.pop("content")
        for content_item_data in _content:

            def _parse_content_item(data: object) -> Union["ImageFile", "Text"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    content_item_type_0 = ImageFile.from_dict(data)

                    return content_item_type_0
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                content_item_type_1 = Text.from_dict(data)

                return content_item_type_1

            content_item = _parse_content_item(content_item_data)

            content.append(content_item)

        file_ids = cast(List[str], d.pop("file_ids"))

        assistant_id = d.pop("assistant_id")

        run_id = d.pop("run_id")

        _metadata = d.pop("metadata")
        metadata: Optional[TheMessageObjectMetadata]
        if _metadata is None:
            metadata = None
        else:
            metadata = TheMessageObjectMetadata.from_dict(_metadata)

        the_message_object = cls(
            id=id,
            object_=object_,
            created_at=created_at,
            thread_id=thread_id,
            role=role,
            content=content,
            file_ids=file_ids,
            assistant_id=assistant_id,
            run_id=run_id,
            metadata=metadata,
        )

        the_message_object.additional_properties = d
        return the_message_object

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
