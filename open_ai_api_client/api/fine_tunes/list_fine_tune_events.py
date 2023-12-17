from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_fine_tune_events_response import ListFineTuneEventsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    fine_tune_id: str,
    *,
    stream: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}
    params["stream"] = stream

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": "/fine-tunes/{fine_tune_id}/events".format(
            fine_tune_id=fine_tune_id,
        ),
        "params": params,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ListFineTuneEventsResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListFineTuneEventsResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ListFineTuneEventsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    fine_tune_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    stream: Union[Unset, None, bool] = False,
) -> Response[ListFineTuneEventsResponse]:
    """Get fine-grained status updates for a fine-tune job.

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.
        stream (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFineTuneEventsResponse]
    """

    kwargs = _get_kwargs(
        fine_tune_id=fine_tune_id,
        stream=stream,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fine_tune_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    stream: Union[Unset, None, bool] = False,
) -> Optional[ListFineTuneEventsResponse]:
    """Get fine-grained status updates for a fine-tune job.

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.
        stream (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListFineTuneEventsResponse
    """

    return sync_detailed(
        fine_tune_id=fine_tune_id,
        client=client,
        stream=stream,
    ).parsed


async def asyncio_detailed(
    fine_tune_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    stream: Union[Unset, None, bool] = False,
) -> Response[ListFineTuneEventsResponse]:
    """Get fine-grained status updates for a fine-tune job.

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.
        stream (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListFineTuneEventsResponse]
    """

    kwargs = _get_kwargs(
        fine_tune_id=fine_tune_id,
        stream=stream,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fine_tune_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    stream: Union[Unset, None, bool] = False,
) -> Optional[ListFineTuneEventsResponse]:
    """Get fine-grained status updates for a fine-tune job.

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.
        stream (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListFineTuneEventsResponse
    """

    return (
        await asyncio_detailed(
            fine_tune_id=fine_tune_id,
            client=client,
            stream=stream,
        )
    ).parsed
