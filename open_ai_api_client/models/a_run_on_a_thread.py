from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.a_run_on_a_thread_object import ARunOnAThreadObject
from ..models.a_run_on_a_thread_status import ARunOnAThreadStatus

if TYPE_CHECKING:
    from ..models.a_run_on_a_thread_last_error import ARunOnAThreadLastError
    from ..models.a_run_on_a_thread_metadata import ARunOnAThreadMetadata
    from ..models.a_run_on_a_thread_required_action import ARunOnAThreadRequiredAction
    from ..models.code_interpreter_tool import CodeInterpreterTool
    from ..models.function_tool import FunctionTool
    from ..models.retrieval_tool import RetrievalTool


T = TypeVar("T", bound="ARunOnAThread")


@_attrs_define
class ARunOnAThread:
    """Represents an execution run on a [thread](/docs/api-reference/threads).

    Attributes:
        id (str): The identifier, which can be referenced in API endpoints.
        object_ (ARunOnAThreadObject): The object type, which is always `thread.run`.
        created_at (int): The Unix timestamp (in seconds) for when the run was created.
        thread_id (str): The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.
        assistant_id (str): The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.
        status (ARunOnAThreadStatus): The status of the run, which can be either `queued`, `in_progress`,
            `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, or `expired`.
        expires_at (int): The Unix timestamp (in seconds) for when the run will expire.
        model (str): The model that the [assistant](/docs/api-reference/assistants) used for this run.
        instructions (str): The instructions that the [assistant](/docs/api-reference/assistants) used for this run.
        tools (List[Union['CodeInterpreterTool', 'FunctionTool', 'RetrievalTool']]): The list of tools that the
            [assistant](/docs/api-reference/assistants) used for this run.
        file_ids (List[str]): The list of [File](/docs/api-reference/files) IDs the [assistant](/docs/api-
            reference/assistants) used for this run.
        required_action (Optional[ARunOnAThreadRequiredAction]): Details on the action required to continue the run.
            Will be `null` if no action is required.
        last_error (Optional[ARunOnAThreadLastError]): The last error associated with this run. Will be `null` if there
            are no errors.
        started_at (Optional[int]): The Unix timestamp (in seconds) for when the run was started.
        cancelled_at (Optional[int]): The Unix timestamp (in seconds) for when the run was cancelled.
        failed_at (Optional[int]): The Unix timestamp (in seconds) for when the run failed.
        completed_at (Optional[int]): The Unix timestamp (in seconds) for when the run was completed.
        metadata (Optional[ARunOnAThreadMetadata]): Set of 16 key-value pairs that can be attached to an object. This
            can be useful for storing additional information about the object in a structured format. Keys can be a maximum
            of 64 characters long and values can be a maxium of 512 characters long.
    """

    id: str
    object_: ARunOnAThreadObject
    created_at: int
    thread_id: str
    assistant_id: str
    status: ARunOnAThreadStatus
    expires_at: int
    model: str
    instructions: str
    tools: List[Union["CodeInterpreterTool", "FunctionTool", "RetrievalTool"]]
    file_ids: List[str]
    required_action: Optional["ARunOnAThreadRequiredAction"]
    last_error: Optional["ARunOnAThreadLastError"]
    started_at: Optional[int]
    cancelled_at: Optional[int]
    failed_at: Optional[int]
    completed_at: Optional[int]
    metadata: Optional["ARunOnAThreadMetadata"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.code_interpreter_tool import CodeInterpreterTool
        from ..models.retrieval_tool import RetrievalTool

        id = self.id
        object_ = self.object_.value

        created_at = self.created_at
        thread_id = self.thread_id
        assistant_id = self.assistant_id
        status = self.status.value

        expires_at = self.expires_at
        model = self.model
        instructions = self.instructions
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

        required_action = self.required_action.to_dict() if self.required_action else None

        last_error = self.last_error.to_dict() if self.last_error else None

        started_at = self.started_at
        cancelled_at = self.cancelled_at
        failed_at = self.failed_at
        completed_at = self.completed_at
        metadata = self.metadata.to_dict() if self.metadata else None

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "object": object_,
                "created_at": created_at,
                "thread_id": thread_id,
                "assistant_id": assistant_id,
                "status": status,
                "expires_at": expires_at,
                "model": model,
                "instructions": instructions,
                "tools": tools,
                "file_ids": file_ids,
                "required_action": required_action,
                "last_error": last_error,
                "started_at": started_at,
                "cancelled_at": cancelled_at,
                "failed_at": failed_at,
                "completed_at": completed_at,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.a_run_on_a_thread_last_error import ARunOnAThreadLastError
        from ..models.a_run_on_a_thread_metadata import ARunOnAThreadMetadata
        from ..models.a_run_on_a_thread_required_action import ARunOnAThreadRequiredAction
        from ..models.code_interpreter_tool import CodeInterpreterTool
        from ..models.function_tool import FunctionTool
        from ..models.retrieval_tool import RetrievalTool

        d = src_dict.copy()
        id = d.pop("id")

        object_ = ARunOnAThreadObject(d.pop("object"))

        created_at = d.pop("created_at")

        thread_id = d.pop("thread_id")

        assistant_id = d.pop("assistant_id")

        status = ARunOnAThreadStatus(d.pop("status"))

        expires_at = d.pop("expires_at")

        model = d.pop("model")

        instructions = d.pop("instructions")

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

        _required_action = d.pop("required_action")
        required_action: Optional[ARunOnAThreadRequiredAction]
        if _required_action is None:
            required_action = None
        else:
            required_action = ARunOnAThreadRequiredAction.from_dict(_required_action)

        _last_error = d.pop("last_error")
        last_error: Optional[ARunOnAThreadLastError]
        if _last_error is None:
            last_error = None
        else:
            last_error = ARunOnAThreadLastError.from_dict(_last_error)

        started_at = d.pop("started_at")

        cancelled_at = d.pop("cancelled_at")

        failed_at = d.pop("failed_at")

        completed_at = d.pop("completed_at")

        _metadata = d.pop("metadata")
        metadata: Optional[ARunOnAThreadMetadata]
        if _metadata is None:
            metadata = None
        else:
            metadata = ARunOnAThreadMetadata.from_dict(_metadata)

        a_run_on_a_thread = cls(
            id=id,
            object_=object_,
            created_at=created_at,
            thread_id=thread_id,
            assistant_id=assistant_id,
            status=status,
            expires_at=expires_at,
            model=model,
            instructions=instructions,
            tools=tools,
            file_ids=file_ids,
            required_action=required_action,
            last_error=last_error,
            started_at=started_at,
            cancelled_at=cancelled_at,
            failed_at=failed_at,
            completed_at=completed_at,
            metadata=metadata,
        )

        a_run_on_a_thread.additional_properties = d
        return a_run_on_a_thread

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
