from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_interpreter_tool import CodeInterpreterTool
    from ..models.function_tool import FunctionTool
    from ..models.modify_assistant_request_metadata import ModifyAssistantRequestMetadata
    from ..models.retrieval_tool import RetrievalTool


T = TypeVar("T", bound="ModifyAssistantRequest")


@_attrs_define
class ModifyAssistantRequest:
    """
    Attributes:
        model (Union[Unset, str]): ID of the model to use. You can use the [List models](/docs/api-
            reference/models/list) API to see all of your available models, or see our [Model
            overview](/docs/models/overview) for descriptions of them.
        name (Union[Unset, None, str]): The name of the assistant. The maximum length is 256 characters.
        description (Union[Unset, None, str]): The description of the assistant. The maximum length is 512 characters.
        instructions (Union[Unset, None, str]): The system instructions that the assistant uses. The maximum length is
            32768 characters.
        tools (Union[Unset, List[Union['CodeInterpreterTool', 'FunctionTool', 'RetrievalTool']]]): A list of tool
            enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types
            `code_interpreter`, `retrieval`, or `function`.
        file_ids (Union[Unset, List[str]]): A list of [File](/docs/api-reference/files) IDs attached to this assistant.
            There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in
            ascending order. If a file was previosuly attached to the list but does not show up in the list, it will be
            deleted from the assistant.
        metadata (Union[Unset, None, ModifyAssistantRequestMetadata]): Set of 16 key-value pairs that can be attached to
            an object. This can be useful for storing additional information about the object in a structured format. Keys
            can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    model: Union[Unset, str] = UNSET
    name: Union[Unset, None, str] = UNSET
    description: Union[Unset, None, str] = UNSET
    instructions: Union[Unset, None, str] = UNSET
    tools: Union[Unset, List[Union["CodeInterpreterTool", "FunctionTool", "RetrievalTool"]]] = UNSET
    file_ids: Union[Unset, List[str]] = UNSET
    metadata: Union[Unset, None, "ModifyAssistantRequestMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.code_interpreter_tool import CodeInterpreterTool
        from ..models.retrieval_tool import RetrievalTool

        model: Union[Unset, str]
        if isinstance(self.model, Unset):
            model = UNSET

        else:
            model = self.model

        name = self.name
        description = self.description
        instructions = self.instructions
        tools: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tools, Unset):
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

        file_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.file_ids, Unset):
            file_ids = self.file_ids

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update({})
        if model is not UNSET:
            field_dict["model"] = model
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if tools is not UNSET:
            field_dict["tools"] = tools
        if file_ids is not UNSET:
            field_dict["file_ids"] = file_ids
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_interpreter_tool import CodeInterpreterTool
        from ..models.function_tool import FunctionTool
        from ..models.modify_assistant_request_metadata import ModifyAssistantRequestMetadata
        from ..models.retrieval_tool import RetrievalTool

        d = src_dict.copy()

        def _parse_model(data: object) -> Union[Unset, str]:
            if isinstance(data, Unset):
                return data
            return cast(Union[Unset, str], data)

        model = _parse_model(d.pop("model", UNSET))

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        instructions = d.pop("instructions", UNSET)

        tools = []
        _tools = d.pop("tools", UNSET)
        for tools_item_data in _tools or []:

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

        file_ids = cast(List[str], d.pop("file_ids", UNSET))

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, ModifyAssistantRequestMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ModifyAssistantRequestMetadata.from_dict(_metadata)

        modify_assistant_request = cls(
            model=model,
            name=name,
            description=description,
            instructions=instructions,
            tools=tools,
            file_ids=file_ids,
            metadata=metadata,
        )

        return modify_assistant_request
