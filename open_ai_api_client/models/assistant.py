from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.assistant_object import AssistantObject

if TYPE_CHECKING:
    from ..models.assistant_metadata import AssistantMetadata
    from ..models.code_interpreter_tool import CodeInterpreterTool
    from ..models.function_tool import FunctionTool
    from ..models.retrieval_tool import RetrievalTool


T = TypeVar("T", bound="Assistant")


@_attrs_define
class Assistant:
    """Represents an `assistant` that can call the model and use tools.

    Attributes:
        id (str): The identifier, which can be referenced in API endpoints.
        object_ (AssistantObject): The object type, which is always `assistant`.
        created_at (int): The Unix timestamp (in seconds) for when the assistant was created.
        model (str): ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see
            all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.
        tools (List[Union['CodeInterpreterTool', 'FunctionTool', 'RetrievalTool']]): A list of tool enabled on the
            assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`,
            `retrieval`, or `function`.
        file_ids (List[str]): A list of [file](/docs/api-reference/files) IDs attached to this assistant. There can be a
            maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.
        name (Optional[str]): The name of the assistant. The maximum length is 256 characters.
        description (Optional[str]): The description of the assistant. The maximum length is 512 characters.
        instructions (Optional[str]): The system instructions that the assistant uses. The maximum length is 32768
            characters.
        metadata (Optional[AssistantMetadata]): Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured format. Keys can be a maximum of 64
            characters long and values can be a maxium of 512 characters long.
    """

    id: str
    object_: AssistantObject
    created_at: int
    model: str
    tools: List[Union["CodeInterpreterTool", "FunctionTool", "RetrievalTool"]]
    file_ids: List[str]
    name: Optional[str]
    description: Optional[str]
    instructions: Optional[str]
    metadata: Optional["AssistantMetadata"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.code_interpreter_tool import CodeInterpreterTool
        from ..models.retrieval_tool import RetrievalTool

        id = self.id
        object_ = self.object_.value

        created_at = self.created_at
        model = self.model
        tools = []
        for tools_item_data in self.tools:
            tools_item: Dict[str, Any]

            if isinstance(tools_item_data, CodeInterpreterTool):
                tools_item = tools_item_data.to_dict()

            elif isinstance(tools_item_data, RetrievalTool):
                tools_item = tools_item_data.to_dict()

            else:
                tools_item = tools_item_data.to_dict()

            tools.append(tools_item)

        file_ids = self.file_ids

        name = self.name
        description = self.description
        instructions = self.instructions
        metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created_at": created_at,
                "model": model,
                "tools": tools,
                "file_ids": file_ids,
                "name": name,
                "description": description,
                "instructions": instructions,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.assistant_metadata import AssistantMetadata
        from ..models.code_interpreter_tool import CodeInterpreterTool
        from ..models.function_tool import FunctionTool
        from ..models.retrieval_tool import RetrievalTool

        d = src_dict.copy()
        id = d.pop("id")

        object_ = AssistantObject(d.pop("object"))

        created_at = d.pop("created_at")

        model = d.pop("model")

        tools = []
        _tools = d.pop("tools")
        for tools_item_data in _tools:

            def _parse_tools_item(data: object) -> Union["CodeInterpreterTool", "FunctionTool", "RetrievalTool"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_0 = CodeInterpreterTool.from_dict(data)

                    return tools_item_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    tools_item_type_1 = RetrievalTool.from_dict(data)

                    return tools_item_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                tools_item_type_2 = FunctionTool.from_dict(data)

                return tools_item_type_2

            tools_item = _parse_tools_item(tools_item_data)

            tools.append(tools_item)

        file_ids = cast(List[str], d.pop("file_ids"))

        name = d.pop("name")

        description = d.pop("description")

        instructions = d.pop("instructions")

        _metadata = d.pop("metadata")
        metadata: Optional[AssistantMetadata]
        if _metadata is None:
            metadata = None
        else:
            metadata = AssistantMetadata.from_dict(_metadata)

        assistant = cls(
            id=id,
            object_=object_,
            created_at=created_at,
            model=model,
            tools=tools,
            file_ids=file_ids,
            name=name,
            description=description,
            instructions=instructions,
            metadata=metadata,
        )

        assistant.additional_properties = d
        return assistant

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
