from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fine_tune import FineTune
from ...types import Response


def _get_kwargs(
    fine_tune_id: str,
) -> Dict[str, Any]:
    return {
        "method": "post",
        "url": "/fine-tunes/{fine_tune_id}/cancel".format(
            fine_tune_id=fine_tune_id,
        ),
    }


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[FineTune]:
    if response.status_code == HTTPStatus.OK:
        response_200 = FineTune.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[FineTune]:
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
) -> Response[FineTune]:
    """Immediately cancel a fine-tune job.

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FineTune]
    """

    kwargs = _get_kwargs(
        fine_tune_id=fine_tune_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    fine_tune_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[FineTune]:
    """Immediately cancel a fine-tune job.

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FineTune
    """

    return sync_detailed(
        fine_tune_id=fine_tune_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    fine_tune_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[FineTune]:
    """Immediately cancel a fine-tune job.

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FineTune]
    """

    kwargs = _get_kwargs(
        fine_tune_id=fine_tune_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    fine_tune_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[FineTune]:
    """Immediately cancel a fine-tune job.

    Args:
        fine_tune_id (str):  Example: ft-AF1WoRqd3aJAHsqc9NY7iL8F.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FineTune
    """

    return (
        await asyncio_detailed(
            fine_tune_id=fine_tune_id,
            client=client,
        )
    ).parsed
