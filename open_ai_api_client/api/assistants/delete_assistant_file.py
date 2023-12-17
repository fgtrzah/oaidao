from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_assistant_file_response import DeleteAssistantFileResponse
from ...types import Response


def _get_kwargs(
    assistant_id: str,
    file_id: str,
) -> Dict[str, Any]:
    return {
        "method": "delete",
        "url": "/assistants/{assistant_id}/files/{file_id}".format(
            assistant_id=assistant_id,
            file_id=file_id,
        ),
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteAssistantFileResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DeleteAssistantFileResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteAssistantFileResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    assistant_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteAssistantFileResponse]:
    """Delete an assistant file.

    Args:
        assistant_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAssistantFileResponse]
    """

    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    assistant_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteAssistantFileResponse]:
    """Delete an assistant file.

    Args:
        assistant_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAssistantFileResponse
    """

    return sync_detailed(
        assistant_id=assistant_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    assistant_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteAssistantFileResponse]:
    """Delete an assistant file.

    Args:
        assistant_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteAssistantFileResponse]
    """

    kwargs = _get_kwargs(
        assistant_id=assistant_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    assistant_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteAssistantFileResponse]:
    """Delete an assistant file.

    Args:
        assistant_id (str):
        file_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteAssistantFileResponse
    """

    return (
        await asyncio_detailed(
            assistant_id=assistant_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
