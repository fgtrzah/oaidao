from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.modify_message_request import ModifyMessageRequest
from ...models.the_message_object import TheMessageObject
from ...types import Response


def _get_kwargs(
    thread_id: str,
    message_id: str,
    *,
    json_body: ModifyMessageRequest,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/threads/{thread_id}/messages/{message_id}".format(
            thread_id=thread_id,
            message_id=message_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[TheMessageObject]:
    if response.status_code == HTTPStatus.OK:
        response_200 = TheMessageObject.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[TheMessageObject]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    thread_id: str,
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ModifyMessageRequest,
) -> Response[TheMessageObject]:
    """Modifies a message.

    Args:
        thread_id (str):
        message_id (str):
        json_body (ModifyMessageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TheMessageObject]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        message_id=message_id,
        json_body=json_body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    thread_id: str,
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ModifyMessageRequest,
) -> Optional[TheMessageObject]:
    """Modifies a message.

    Args:
        thread_id (str):
        message_id (str):
        json_body (ModifyMessageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TheMessageObject
    """

    return sync_detailed(
        thread_id=thread_id,
        message_id=message_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ModifyMessageRequest,
) -> Response[TheMessageObject]:
    """Modifies a message.

    Args:
        thread_id (str):
        message_id (str):
        json_body (ModifyMessageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TheMessageObject]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        message_id=message_id,
        json_body=json_body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    json_body: ModifyMessageRequest,
) -> Optional[TheMessageObject]:
    """Modifies a message.

    Args:
        thread_id (str):
        message_id (str):
        json_body (ModifyMessageRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TheMessageObject
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            message_id=message_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
