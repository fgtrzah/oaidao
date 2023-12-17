from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.create_edit_request_model_type_1 import CreateEditRequestModelType1
from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateEditRequest")


@_attrs_define
class CreateEditRequest:
    """
    Attributes:
        instruction (str): The instruction that tells the model how to edit the prompt. Example: Fix the spelling
            mistakes..
        model (Union[CreateEditRequestModelType1, str]): ID of the model to use. You can use the `text-davinci-edit-001`
            or `code-davinci-edit-001` model with this endpoint. Example: text-davinci-edit-001.
        input_ (Union[Unset, None, str]): The input text to use as a starting point for the edit. Default: ''. Example:
            What day of the wek is it?.
        n (Union[Unset, None, int]): How many edits to generate for the input and instruction. Default: 1. Example: 1.
        temperature (Union[Unset, None, float]): What sampling temperature to use, between 0 and 2. Higher values like
            0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

            We generally recommend altering this or `top_p` but not both.
             Default: 1.0. Example: 1.
        top_p (Union[Unset, None, float]): An alternative to sampling with temperature, called nucleus sampling, where
            the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens
            comprising the top 10% probability mass are considered.

            We generally recommend altering this or `temperature` but not both.
             Default: 1.0. Example: 1.
    """

    instruction: str
    model: Union[CreateEditRequestModelType1, str]
    input_: Union[Unset, None, str] = ""
    n: Union[Unset, None, int] = 1
    temperature: Union[Unset, None, float] = 1.0
    top_p: Union[Unset, None, float] = 1.0
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        instruction = self.instruction
        model: str

        if isinstance(self.model, CreateEditRequestModelType1):
            model = self.model.value

        else:
            model = self.model

        input_ = self.input_
        n = self.n
        temperature = self.temperature
        top_p = self.top_p

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "instruction": instruction,
                "model": model,
            }
        )
        if input_ is not UNSET:
            field_dict["input"] = input_
        if n is not UNSET:
            field_dict["n"] = n
        if temperature is not UNSET:
            field_dict["temperature"] = temperature
        if top_p is not UNSET:
            field_dict["top_p"] = top_p

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        instruction = d.pop("instruction")

        def _parse_model(data: object) -> Union[CreateEditRequestModelType1, str]:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                model_type_1 = CreateEditRequestModelType1(data)

                return model_type_1
            except:  # noqa: E722
                pass
            return cast(Union[CreateEditRequestModelType1, str], data)

        model = _parse_model(d.pop("model"))

        input_ = d.pop("input", UNSET)

        n = d.pop("n", UNSET)

        temperature = d.pop("temperature", UNSET)

        top_p = d.pop("top_p", UNSET)

        create_edit_request = cls(
            instruction=instruction,
            model=model,
            input_=input_,
            n=n,
            temperature=temperature,
            top_p=top_p,
        )

        create_edit_request.additional_properties = d
        return create_edit_request

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
