from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Image")


@_attrs_define
class Image:
    """Represents the url or the content of an image generated by the OpenAI API.

    Attributes:
        b64_json (Union[Unset, str]): The base64-encoded JSON of the generated image, if `response_format` is
            `b64_json`.
        url (Union[Unset, str]): The URL of the generated image, if `response_format` is `url` (default).
        revised_prompt (Union[Unset, str]): The prompt that was used to generate the image, if there was any revision to
            the prompt.
    """

    b64_json: Union[Unset, str] = UNSET
    url: Union[Unset, str] = UNSET
    revised_prompt: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        b64_json = self.b64_json
        url = self.url
        revised_prompt = self.revised_prompt

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if b64_json is not UNSET:
            field_dict["b64_json"] = b64_json
        if url is not UNSET:
            field_dict["url"] = url
        if revised_prompt is not UNSET:
            field_dict["revised_prompt"] = revised_prompt

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        b64_json = d.pop("b64_json", UNSET)

        url = d.pop("url", UNSET)

        revised_prompt = d.pop("revised_prompt", UNSET)

        image = cls(
            b64_json=b64_json,
            url=url,
            revised_prompt=revised_prompt,
        )

        image.additional_properties = d
        return image

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
