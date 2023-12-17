from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_image_edit_request import CreateImageEditRequest
from ...models.images_response import ImagesResponse
from ...types import Response


def _get_kwargs(
    *,
    multipart_data: CreateImageEditRequest,
) -> Dict[str, Any]:
    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": "/images/edits",
        "files": multipart_multipart_data,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ImagesResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ImagesResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ImagesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: CreateImageEditRequest,
) -> Response[ImagesResponse]:
    """Creates an edited or extended image given an original image and a prompt.

    Args:
        multipart_data (CreateImageEditRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImagesResponse]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: CreateImageEditRequest,
) -> Optional[ImagesResponse]:
    """Creates an edited or extended image given an original image and a prompt.

    Args:
        multipart_data (CreateImageEditRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImagesResponse
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: CreateImageEditRequest,
) -> Response[ImagesResponse]:
    """Creates an edited or extended image given an original image and a prompt.

    Args:
        multipart_data (CreateImageEditRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImagesResponse]
    """

    kwargs = _get_kwargs(
        multipart_data=multipart_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    multipart_data: CreateImageEditRequest,
) -> Optional[ImagesResponse]:
    """Creates an edited or extended image given an original image and a prompt.

    Args:
        multipart_data (CreateImageEditRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImagesResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
