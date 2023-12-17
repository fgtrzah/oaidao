from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assistant import Assistant
from ...models.modify_assistant_request import ModifyAssistantRequest
from ...types import Response


def _get_kwargs(
    assistant_id: str,
    *,
    json_body: ModifyAssistantRequest,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/assistants/{assistant_id}".format(
            assistant_id=assistant_id,
        ),
        "json": json_json_body,
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Assistant]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Assistant.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Assistant]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assistant_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ModifyAssistantRequest,
) -> Response[Assistant]:
    """Modifies an assistant.

    Args:
        assistant_id (str):
        json_body (ModifyAssistantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Assistant]
    """

    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assistant_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ModifyAssistantRequest,
) -> Optional[Assistant]:
    """Modifies an assistant.

    Args:
        assistant_id (str):
        json_body (ModifyAssistantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Assistant
    """

    return sync_detailed(
        assistant_id=assistant_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    assistant_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ModifyAssistantRequest,
) -> Response[Assistant]:
    """Modifies an assistant.

    Args:
        assistant_id (str):
        json_body (ModifyAssistantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Assistant]
    """

    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assistant_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ModifyAssistantRequest,
) -> Optional[Assistant]:
    """Modifies an assistant.

    Args:
        assistant_id (str):
        json_body (ModifyAssistantRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Assistant
    """

    return (
        await asyncio_detailed(
            assistant_id=assistant_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
