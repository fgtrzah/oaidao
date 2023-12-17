from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.code_interpreter_tool import CodeInterpreterTool
    from ..models.create_thread_and_run_request_metadata import CreateThreadAndRunRequestMetadata
    from ..models.create_thread_request import CreateThreadRequest
    from ..models.function_tool import FunctionTool
    from ..models.retrieval_tool import RetrievalTool


T = TypeVar("T", bound="CreateThreadAndRunRequest")


@_attrs_define
class CreateThreadAndRunRequest:
    """
    Attributes:
        assistant_id (str): The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.
        thread (Union[Unset, CreateThreadRequest]):
        model (Union[Unset, None, str]): The ID of the [Model](/docs/api-reference/models) to be used to execute this
            run. If a value is provided here, it will override the model associated with the assistant. If not, the model
            associated with the assistant will be used.
        instructions (Union[Unset, None, str]): Override the default system message of the assistant. This is useful for
            modifying the behavior on a per-run basis.
        tools (Union[Unset, None, List[Union['CodeInterpreterTool', 'FunctionTool', 'RetrievalTool']]]): Override the
            tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.
        metadata (Union[Unset, None, CreateThreadAndRunRequestMetadata]): Set of 16 key-value pairs that can be attached
            to an object. This can be useful for storing additional information about the object in a structured format.
            Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    assistant_id: str
    thread: Union[Unset, "CreateThreadRequest"] = UNSET
    model: Union[Unset, None, str] = UNSET
    instructions: Union[Unset, None, str] = UNSET
    tools: Union[Unset, None, List[Union["CodeInterpreterTool", "FunctionTool", "RetrievalTool"]]] = UNSET
    metadata: Union[Unset, None, "CreateThreadAndRunRequestMetadata"] = UNSET

    def to_dict(self) -> Dict[str, Any]:
        from ..models.code_interpreter_tool import CodeInterpreterTool
        from ..models.retrieval_tool import RetrievalTool

        assistant_id = self.assistant_id
        thread: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.thread, Unset):
            thread = self.thread.to_dict()

        model = self.model
        instructions = self.instructions
        tools: Union[Unset, None, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.tools, Unset):
            if self.tools is None:
                tools = None
            else:
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

        metadata: Union[Unset, None, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(
            {
                "assistant_id": assistant_id,
            }
        )
        if thread is not UNSET:
            field_dict["thread"] = thread
        if model is not UNSET:
            field_dict["model"] = model
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if tools is not UNSET:
            field_dict["tools"] = tools
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.code_interpreter_tool import CodeInterpreterTool
        from ..models.create_thread_and_run_request_metadata import CreateThreadAndRunRequestMetadata
        from ..models.create_thread_request import CreateThreadRequest
        from ..models.function_tool import FunctionTool
        from ..models.retrieval_tool import RetrievalTool

        d = src_dict.copy()
        assistant_id = d.pop("assistant_id")

        _thread = d.pop("thread", UNSET)
        thread: Union[Unset, CreateThreadRequest]
        if isinstance(_thread, Unset):
            thread = UNSET
        else:
            thread = CreateThreadRequest.from_dict(_thread)

        model = d.pop("model", UNSET)

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

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, None, CreateThreadAndRunRequestMetadata]
        if _metadata is None:
            metadata = None
        elif isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CreateThreadAndRunRequestMetadata.from_dict(_metadata)

        create_thread_and_run_request = cls(
            assistant_id=assistant_id,
            thread=thread,
            model=model,
            instructions=instructions,
            tools=tools,
            metadata=metadata,
        )

        return create_thread_and_run_request
