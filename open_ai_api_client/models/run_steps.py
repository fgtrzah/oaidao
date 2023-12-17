from typing import TYPE_CHECKING, Any, Dict, List, Optional, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.run_steps_object import RunStepsObject
from ..models.run_steps_status import RunStepsStatus
from ..models.run_steps_type import RunStepsType

if TYPE_CHECKING:
    from ..models.message_creation import MessageCreation
    from ..models.run_steps_last_error import RunStepsLastError
    from ..models.run_steps_metadata import RunStepsMetadata
    from ..models.tool_calls import ToolCalls


T = TypeVar("T", bound="RunSteps")


@_attrs_define
class RunSteps:
    """Represents a step in execution of a run.

    Attributes:
        id (str): The identifier of the run step, which can be referenced in API endpoints.
        object_ (RunStepsObject): The object type, which is always `thread.run.step`.
        created_at (int): The Unix timestamp (in seconds) for when the run step was created.
        assistant_id (str): The ID of the [assistant](/docs/api-reference/assistants) associated with the run step.
        thread_id (str): The ID of the [thread](/docs/api-reference/threads) that was run.
        run_id (str): The ID of the [run](/docs/api-reference/runs) that this run step is a part of.
        type (RunStepsType): The type of run step, which can be either `message_creation` or `tool_calls`.
        status (RunStepsStatus): The status of the run step, which can be either `in_progress`, `cancelled`, `failed`,
            `completed`, or `expired`.
        step_details (Union['MessageCreation', 'ToolCalls']): The details of the run step.
        last_error (Optional[RunStepsLastError]): The last error associated with this run step. Will be `null` if there
            are no errors.
        expired_at (Optional[int]): The Unix timestamp (in seconds) for when the run step expired. A step is considered
            expired if the parent run is expired.
        cancelled_at (Optional[int]): The Unix timestamp (in seconds) for when the run step was cancelled.
        failed_at (Optional[int]): The Unix timestamp (in seconds) for when the run step failed.
        completed_at (Optional[int]): The Unix timestamp (in seconds) for when the run step completed.
        metadata (Optional[RunStepsMetadata]): Set of 16 key-value pairs that can be attached to an object. This can be
            useful for storing additional information about the object in a structured format. Keys can be a maximum of 64
            characters long and values can be a maxium of 512 characters long.
    """

    id: str
    object_: RunStepsObject
    created_at: int
    assistant_id: str
    thread_id: str
    run_id: str
    type: RunStepsType
    status: RunStepsStatus
    step_details: Union["MessageCreation", "ToolCalls"]
    last_error: Optional["RunStepsLastError"]
    expired_at: Optional[int]
    cancelled_at: Optional[int]
    failed_at: Optional[int]
    completed_at: Optional[int]
    metadata: Optional["RunStepsMetadata"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.message_creation import MessageCreation

        id = self.id
        object_ = self.object_.value

        created_at = self.created_at
        assistant_id = self.assistant_id
        thread_id = self.thread_id
        run_id = self.run_id
        type = self.type.value

        status = self.status.value

        step_details: Dict[str, Any]

        if isinstance(self.step_details, MessageCreation):
            step_details = self.step_details.to_dict()

        else:
            step_details = self.step_details.to_dict()

        last_error = self.last_error.to_dict() if self.last_error else None

        expired_at = self.expired_at
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
                "assistant_id": assistant_id,
                "thread_id": thread_id,
                "run_id": run_id,
                "type": type,
                "status": status,
                "step_details": step_details,
                "last_error": last_error,
                "expired_at": expired_at,
                "cancelled_at": cancelled_at,
                "failed_at": failed_at,
                "completed_at": completed_at,
                "metadata": metadata,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.message_creation import MessageCreation
        from ..models.run_steps_last_error import RunStepsLastError
        from ..models.run_steps_metadata import RunStepsMetadata
        from ..models.tool_calls import ToolCalls

        d = src_dict.copy()
        id = d.pop("id")

        object_ = RunStepsObject(d.pop("object"))

        created_at = d.pop("created_at")

        assistant_id = d.pop("assistant_id")

        thread_id = d.pop("thread_id")

        run_id = d.pop("run_id")

        type = RunStepsType(d.pop("type"))

        status = RunStepsStatus(d.pop("status"))

        def _parse_step_details(data: object) -> Union["MessageCreation", "ToolCalls"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                step_details_type_0 = MessageCreation.from_dict(data)

                return step_details_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            step_details_type_1 = ToolCalls.from_dict(data)

            return step_details_type_1

        step_details = _parse_step_details(d.pop("step_details"))

        _last_error = d.pop("last_error")
        last_error: Optional[RunStepsLastError]
        if _last_error is None:
            last_error = None
        else:
            last_error = RunStepsLastError.from_dict(_last_error)

        expired_at = d.pop("expired_at")

        cancelled_at = d.pop("cancelled_at")

        failed_at = d.pop("failed_at")

        completed_at = d.pop("completed_at")

        _metadata = d.pop("metadata")
        metadata: Optional[RunStepsMetadata]
        if _metadata is None:
            metadata = None
        else:
            metadata = RunStepsMetadata.from_dict(_metadata)

        run_steps = cls(
            id=id,
            object_=object_,
            created_at=created_at,
            assistant_id=assistant_id,
            thread_id=thread_id,
            run_id=run_id,
            type=type,
            status=status,
            step_details=step_details,
            last_error=last_error,
            expired_at=expired_at,
            cancelled_at=cancelled_at,
            failed_at=failed_at,
            completed_at=completed_at,
            metadata=metadata,
        )

        run_steps.additional_properties = d
        return run_steps

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
