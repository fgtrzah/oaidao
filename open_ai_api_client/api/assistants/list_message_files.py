from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_message_files_order import ListMessageFilesOrder
from ...models.list_message_files_response import ListMessageFilesResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    thread_id: str,
    message_id: str,
    *,
    limit: Union[Unset, None, int] = 20,
    order: Union[Unset, None, ListMessageFilesOrder] = ListMessageFilesOrder.DESC,
    after: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["limit"] = limit

    json_order: Union[Unset, None, str] = UNSET
    if not isinstance(order, Unset):
        json_order = order.value if order else None

    params["order"] = json_order

    params["after"] = after

    params["before"] = before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/threads/{thread_id}/messages/{message_id}/files".format(
            thread_id=thread_id,
            message_id=message_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListMessageFilesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListMessageFilesResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListMessageFilesResponse]:
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
    limit: Union[Unset, None, int] = 20,
    order: Union[Unset, None, ListMessageFilesOrder] = ListMessageFilesOrder.DESC,
    after: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, str] = UNSET,
) -> Response[ListMessageFilesResponse]:
    """Returns a list of message files.

    Args:
        thread_id (str):
        message_id (str):
        limit (Union[Unset, None, int]):  Default: 20.
        order (Union[Unset, None, ListMessageFilesOrder]):  Default: ListMessageFilesOrder.DESC.
        after (Union[Unset, None, str]):
        before (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMessageFilesResponse]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        message_id=message_id,
        limit=limit,
        order=order,
        after=after,
        before=before,
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
    limit: Union[Unset, None, int] = 20,
    order: Union[Unset, None, ListMessageFilesOrder] = ListMessageFilesOrder.DESC,
    after: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, str] = UNSET,
) -> Optional[ListMessageFilesResponse]:
    """Returns a list of message files.

    Args:
        thread_id (str):
        message_id (str):
        limit (Union[Unset, None, int]):  Default: 20.
        order (Union[Unset, None, ListMessageFilesOrder]):  Default: ListMessageFilesOrder.DESC.
        after (Union[Unset, None, str]):
        before (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMessageFilesResponse
    """

    return sync_detailed(
        thread_id=thread_id,
        message_id=message_id,
        client=client,
        limit=limit,
        order=order,
        after=after,
        before=before,
    ).parsed


async def asyncio_detailed(
    thread_id: str,
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = 20,
    order: Union[Unset, None, ListMessageFilesOrder] = ListMessageFilesOrder.DESC,
    after: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, str] = UNSET,
) -> Response[ListMessageFilesResponse]:
    """Returns a list of message files.

    Args:
        thread_id (str):
        message_id (str):
        limit (Union[Unset, None, int]):  Default: 20.
        order (Union[Unset, None, ListMessageFilesOrder]):  Default: ListMessageFilesOrder.DESC.
        after (Union[Unset, None, str]):
        before (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListMessageFilesResponse]
    """

    kwargs = _get_kwargs(
        thread_id=thread_id,
        message_id=message_id,
        limit=limit,
        order=order,
        after=after,
        before=before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    thread_id: str,
    message_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, None, int] = 20,
    order: Union[Unset, None, ListMessageFilesOrder] = ListMessageFilesOrder.DESC,
    after: Union[Unset, None, str] = UNSET,
    before: Union[Unset, None, str] = UNSET,
) -> Optional[ListMessageFilesResponse]:
    """Returns a list of message files.

    Args:
        thread_id (str):
        message_id (str):
        limit (Union[Unset, None, int]):  Default: 20.
        order (Union[Unset, None, ListMessageFilesOrder]):  Default: ListMessageFilesOrder.DESC.
        after (Union[Unset, None, str]):
        before (Union[Unset, None, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListMessageFilesResponse
    """

    return (
        await asyncio_detailed(
            thread_id=thread_id,
            message_id=message_id,
            client=client,
            limit=limit,
            order=order,
            after=after,
            before=before,
        )
    ).parsed
