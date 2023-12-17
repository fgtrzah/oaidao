from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.message_files import MessageFiles
from ...types import Response


def _get_kwargs(
    thread_id: str,
    message_id: str,
    file_id: str,
) -> Dict[str, Any]:
    return {
        "method": "get",
        "url": "/threads/{thread_id}/messages/{message_id}/files/{file_id}".format(
            thread_id=thread_id,
            message_id=message_id,
            file_id=file_id,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[MessageFiles]:
    if response.status_code == HTTPStatus.OK:
        response_200 = MessageFiles.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[MessageFiles]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    message_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MessageFiles]:
    """Retrieves a message file.

    Args:
        thread_id (str):  Example: thread_abc123.
        message_id (str):  Example: msg_abc123.
        file_id (str):  Example: file-abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageFiles]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        message_id=message_id,
        file_id=file_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    message_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MessageFiles]:
    """Retrieves a message file.

    Args:
        thread_id (str):  Example: thread_abc123.
        message_id (str):  Example: msg_abc123.
        file_id (str):  Example: file-abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageFiles
    """

    return sync_detailed(
        thread_id=thread_id,
        message_id=message_id,
        file_id=file_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    message_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[MessageFiles]:
    """Retrieves a message file.

    Args:
        thread_id (str):  Example: thread_abc123.
        message_id (str):  Example: msg_abc123.
        file_id (str):  Example: file-abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[MessageFiles]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        message_id=message_id,
        file_id=file_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    message_id: str,
    file_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[MessageFiles]:
    """Retrieves a message file.

    Args:
        thread_id (str):  Example: thread_abc123.
        message_id (str):  Example: msg_abc123.
        file_id (str):  Example: file-abc123.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        MessageFiles
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            message_id=message_id,
            file_id=file_id,
            client=client,
        )
    ).parsed
