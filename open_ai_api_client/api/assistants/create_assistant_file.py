from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assistant_files import AssistantFiles
from ...models.create_assistant_file_request import CreateAssistantFileRequest
from ...types import Response


def _get_kwargs(
    assistant_id: str,
    *,
    json_body: CreateAssistantFileRequest,
) -> Dict[str, Any]:
    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": "/assistants/{assistant_id}/files".format(
            assistant_id=assistant_id,
        ),
        "json": json_json_body,
    }


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AssistantFiles]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AssistantFiles.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AssistantFiles]:
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
    json_body: CreateAssistantFileRequest,
) -> Response[AssistantFiles]:
    """Create an assistant file by attaching a [File](/docs/api-reference/files) to an
    [assistant](/docs/api-reference/assistants).

    Args:
        assistant_id (str):  Example: file-abc123.
        json_body (CreateAssistantFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssistantFiles]
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
    json_body: CreateAssistantFileRequest,
) -> Optional[AssistantFiles]:
    """Create an assistant file by attaching a [File](/docs/api-reference/files) to an
    [assistant](/docs/api-reference/assistants).

    Args:
        assistant_id (str):  Example: file-abc123.
        json_body (CreateAssistantFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssistantFiles
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
    json_body: CreateAssistantFileRequest,
) -> Response[AssistantFiles]:
    """Create an assistant file by attaching a [File](/docs/api-reference/files) to an
    [assistant](/docs/api-reference/assistants).

    Args:
        assistant_id (str):  Example: file-abc123.
        json_body (CreateAssistantFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AssistantFiles]
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
    json_body: CreateAssistantFileRequest,
) -> Optional[AssistantFiles]:
    """Create an assistant file by attaching a [File](/docs/api-reference/files) to an
    [assistant](/docs/api-reference/assistants).

    Args:
        assistant_id (str):  Example: file-abc123.
        json_body (CreateAssistantFileRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AssistantFiles
    """

    return (
        await asyncio_detailed(
            assistant_id=assistant_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
