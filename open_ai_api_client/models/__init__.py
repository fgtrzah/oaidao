""" Contains all the data models used in inputs/outputs """

from .a_run_on_a_thread import ARunOnAThread
from .a_run_on_a_thread_last_error import ARunOnAThreadLastError
from .a_run_on_a_thread_last_error_code import ARunOnAThreadLastErrorCode
from .a_run_on_a_thread_metadata import ARunOnAThreadMetadata
from .a_run_on_a_thread_object import ARunOnAThreadObject
from .a_run_on_a_thread_required_action import ARunOnAThreadRequiredAction
from .a_run_on_a_thread_required_action_submit_tool_outputs import ARunOnAThreadRequiredActionSubmitToolOutputs
from .a_run_on_a_thread_required_action_type import ARunOnAThreadRequiredActionType
from .a_run_on_a_thread_status import ARunOnAThreadStatus
from .assistant import Assistant
from .assistant_files import AssistantFiles
from .assistant_files_object import AssistantFilesObject
from .assistant_message import AssistantMessage
from .assistant_message_function_call import AssistantMessageFunctionCall
from .assistant_message_role import AssistantMessageRole
from .assistant_metadata import AssistantMetadata
from .assistant_object import AssistantObject
from .chat_completion_function_call_option import ChatCompletionFunctionCallOption
from .chat_completion_functions import ChatCompletionFunctions
from .chat_completion_message_tool_call import ChatCompletionMessageToolCall
from .chat_completion_message_tool_call_chunk import ChatCompletionMessageToolCallChunk
from .chat_completion_message_tool_call_chunk_function import ChatCompletionMessageToolCallChunkFunction
from .chat_completion_message_tool_call_chunk_type import ChatCompletionMessageToolCallChunkType
from .chat_completion_message_tool_call_function import ChatCompletionMessageToolCallFunction
from .chat_completion_message_tool_call_type import ChatCompletionMessageToolCallType
from .chat_completion_named_tool_choice import ChatCompletionNamedToolChoice
from .chat_completion_named_tool_choice_function import ChatCompletionNamedToolChoiceFunction
from .chat_completion_named_tool_choice_type import ChatCompletionNamedToolChoiceType
from .chat_completion_response_message import ChatCompletionResponseMessage
from .chat_completion_response_message_function_call import ChatCompletionResponseMessageFunctionCall
from .chat_completion_response_message_role import ChatCompletionResponseMessageRole
from .chat_completion_role import ChatCompletionRole
from .chat_completion_stream_response_delta import ChatCompletionStreamResponseDelta
from .chat_completion_stream_response_delta_function_call import ChatCompletionStreamResponseDeltaFunctionCall
from .chat_completion_stream_response_delta_role import ChatCompletionStreamResponseDeltaRole
from .chat_completion_token_logprob import ChatCompletionTokenLogprob
from .chat_completion_token_logprob_top_logprobs_item import ChatCompletionTokenLogprobTopLogprobsItem
from .chat_completion_tool import ChatCompletionTool
from .chat_completion_tool_choice_option_type_0 import ChatCompletionToolChoiceOptionType0
from .chat_completion_tool_type import ChatCompletionToolType
from .code_interpreter_image_output import CodeInterpreterImageOutput
from .code_interpreter_image_output_image import CodeInterpreterImageOutputImage
from .code_interpreter_image_output_type import CodeInterpreterImageOutputType
from .code_interpreter_log_output import CodeInterpreterLogOutput
from .code_interpreter_log_output_type import CodeInterpreterLogOutputType
from .code_interpreter_tool import CodeInterpreterTool
from .code_interpreter_tool_call import CodeInterpreterToolCall
from .code_interpreter_tool_call_code_interpreter import CodeInterpreterToolCallCodeInterpreter
from .code_interpreter_tool_call_type import CodeInterpreterToolCallType
from .code_interpreter_tool_type import CodeInterpreterToolType
from .completion_usage import CompletionUsage
from .create_assistant_file_request import CreateAssistantFileRequest
from .create_assistant_request import CreateAssistantRequest
from .create_assistant_request_metadata import CreateAssistantRequestMetadata
from .create_chat_completion_function_response import CreateChatCompletionFunctionResponse
from .create_chat_completion_function_response_choices_item import CreateChatCompletionFunctionResponseChoicesItem
from .create_chat_completion_function_response_choices_item_finish_reason import (
    CreateChatCompletionFunctionResponseChoicesItemFinishReason,
)
from .create_chat_completion_function_response_object import CreateChatCompletionFunctionResponseObject
from .create_chat_completion_image_response import CreateChatCompletionImageResponse
from .create_chat_completion_request import CreateChatCompletionRequest
from .create_chat_completion_request_function_call_type_0 import CreateChatCompletionRequestFunctionCallType0
from .create_chat_completion_request_logit_bias import CreateChatCompletionRequestLogitBias
from .create_chat_completion_request_model_type_1 import CreateChatCompletionRequestModelType1
from .create_chat_completion_request_response_format import CreateChatCompletionRequestResponseFormat
from .create_chat_completion_request_response_format_type import CreateChatCompletionRequestResponseFormatType
from .create_chat_completion_response import CreateChatCompletionResponse
from .create_chat_completion_response_choices_item import CreateChatCompletionResponseChoicesItem
from .create_chat_completion_response_choices_item_finish_reason import (
    CreateChatCompletionResponseChoicesItemFinishReason,
)
from .create_chat_completion_response_choices_item_logprobs import CreateChatCompletionResponseChoicesItemLogprobs
from .create_chat_completion_response_object import CreateChatCompletionResponseObject
from .create_chat_completion_stream_response import CreateChatCompletionStreamResponse
from .create_chat_completion_stream_response_choices_item import CreateChatCompletionStreamResponseChoicesItem
from .create_chat_completion_stream_response_choices_item_finish_reason import (
    CreateChatCompletionStreamResponseChoicesItemFinishReason,
)
from .create_chat_completion_stream_response_choices_item_logprobs import (
    CreateChatCompletionStreamResponseChoicesItemLogprobs,
)
from .create_chat_completion_stream_response_object import CreateChatCompletionStreamResponseObject
from .create_completion_request import CreateCompletionRequest
from .create_completion_request_logit_bias import CreateCompletionRequestLogitBias
from .create_completion_request_model_type_1 import CreateCompletionRequestModelType1
from .create_completion_response import CreateCompletionResponse
from .create_completion_response_choices_item import CreateCompletionResponseChoicesItem
from .create_completion_response_choices_item_finish_reason import CreateCompletionResponseChoicesItemFinishReason
from .create_completion_response_choices_item_logprobs import CreateCompletionResponseChoicesItemLogprobs
from .create_completion_response_choices_item_logprobs_top_logprobs_item import (
    CreateCompletionResponseChoicesItemLogprobsTopLogprobsItem,
)
from .create_completion_response_object import CreateCompletionResponseObject
from .create_edit_request import CreateEditRequest
from .create_edit_request_model_type_1 import CreateEditRequestModelType1
from .create_embedding_request import CreateEmbeddingRequest
from .create_embedding_request_encoding_format import CreateEmbeddingRequestEncodingFormat
from .create_embedding_request_model_type_1 import CreateEmbeddingRequestModelType1
from .create_embedding_response import CreateEmbeddingResponse
from .create_embedding_response_object import CreateEmbeddingResponseObject
from .create_embedding_response_usage import CreateEmbeddingResponseUsage
from .create_file_request import CreateFileRequest
from .create_file_request_purpose import CreateFileRequestPurpose
from .create_image_edit_request import CreateImageEditRequest
from .create_image_edit_request_model_type_1 import CreateImageEditRequestModelType1
from .create_image_edit_request_response_format import CreateImageEditRequestResponseFormat
from .create_image_edit_request_size import CreateImageEditRequestSize
from .create_image_request import CreateImageRequest
from .create_image_request_model_type_1 import CreateImageRequestModelType1
from .create_image_request_quality import CreateImageRequestQuality
from .create_image_request_response_format import CreateImageRequestResponseFormat
from .create_image_request_size import CreateImageRequestSize
from .create_image_request_style import CreateImageRequestStyle
from .create_image_variation_request import CreateImageVariationRequest
from .create_image_variation_request_model_type_1 import CreateImageVariationRequestModelType1
from .create_image_variation_request_response_format import CreateImageVariationRequestResponseFormat
from .create_image_variation_request_size import CreateImageVariationRequestSize
from .create_message_request import CreateMessageRequest
from .create_message_request_metadata import CreateMessageRequestMetadata
from .create_message_request_role import CreateMessageRequestRole
from .create_moderation_request import CreateModerationRequest
from .create_moderation_request_model_type_1 import CreateModerationRequestModelType1
from .create_moderation_response import CreateModerationResponse
from .create_moderation_response_results_item import CreateModerationResponseResultsItem
from .create_moderation_response_results_item_categories import CreateModerationResponseResultsItemCategories
from .create_moderation_response_results_item_category_scores import CreateModerationResponseResultsItemCategoryScores
from .create_run_request import CreateRunRequest
from .create_run_request_metadata import CreateRunRequestMetadata
from .create_speech_request import CreateSpeechRequest
from .create_speech_request_model_type_1 import CreateSpeechRequestModelType1
from .create_speech_request_response_format import CreateSpeechRequestResponseFormat
from .create_speech_request_voice import CreateSpeechRequestVoice
from .create_thread_and_run_request import CreateThreadAndRunRequest
from .create_thread_and_run_request_metadata import CreateThreadAndRunRequestMetadata
from .create_thread_request import CreateThreadRequest
from .create_thread_request_metadata import CreateThreadRequestMetadata
from .create_transcription_request import CreateTranscriptionRequest
from .create_transcription_request_model_type_1 import CreateTranscriptionRequestModelType1
from .create_transcription_request_response_format import CreateTranscriptionRequestResponseFormat
from .create_transcription_response import CreateTranscriptionResponse
from .create_translation_request import CreateTranslationRequest
from .create_translation_request_model_type_1 import CreateTranslationRequestModelType1
from .create_translation_response import CreateTranslationResponse
from .delete_assistant_file_response import DeleteAssistantFileResponse
from .delete_assistant_file_response_object import DeleteAssistantFileResponseObject
from .delete_assistant_response import DeleteAssistantResponse
from .delete_assistant_response_object import DeleteAssistantResponseObject
from .delete_file_response import DeleteFileResponse
from .delete_file_response_object import DeleteFileResponseObject
from .delete_message_response import DeleteMessageResponse
from .delete_message_response_object import DeleteMessageResponseObject
from .delete_model_response import DeleteModelResponse
from .delete_thread_response import DeleteThreadResponse
from .delete_thread_response_object import DeleteThreadResponseObject
from .edit import Edit
from .edit_choices_item import EditChoicesItem
from .edit_choices_item_finish_reason import EditChoicesItemFinishReason
from .edit_object import EditObject
from .embedding import Embedding
from .embedding_object import EmbeddingObject
from .error import Error
from .error_response import ErrorResponse
from .file_citation import FileCitation
from .file_citation_file_citation import FileCitationFileCitation
from .file_citation_type import FileCitationType
from .file_path import FilePath
from .file_path_file_path import FilePathFilePath
from .file_path_type import FilePathType
from .fine_tune import FineTune
from .fine_tune_event import FineTuneEvent
from .fine_tune_event_object import FineTuneEventObject
from .fine_tune_hyperparams import FineTuneHyperparams
from .fine_tune_object import FineTuneObject
from .fine_tuning_job_event import FineTuningJobEvent
from .fine_tuning_job_event_level import FineTuningJobEventLevel
from .fine_tuning_job_event_object import FineTuningJobEventObject
from .function_message import FunctionMessage
from .function_message_role import FunctionMessageRole
from .function_object import FunctionObject
from .function_parameters import FunctionParameters
from .function_tool import FunctionTool
from .function_tool_call import FunctionToolCall
from .function_tool_call_function import FunctionToolCallFunction
from .function_tool_call_type import FunctionToolCallType
from .function_tool_type import FunctionToolType
from .image import Image
from .image_content_part import ImageContentPart
from .image_content_part_image_url import ImageContentPartImageUrl
from .image_content_part_image_url_detail import ImageContentPartImageUrlDetail
from .image_content_part_type import ImageContentPartType
from .image_file import ImageFile
from .image_file_image_file import ImageFileImageFile
from .image_file_type import ImageFileType
from .images_response import ImagesResponse
from .list_assistant_files_order import ListAssistantFilesOrder
from .list_assistant_files_response import ListAssistantFilesResponse
from .list_assistants_order import ListAssistantsOrder
from .list_assistants_response import ListAssistantsResponse
from .list_files_response import ListFilesResponse
from .list_files_response_object import ListFilesResponseObject
from .list_fine_tune_events_response import ListFineTuneEventsResponse
from .list_fine_tune_events_response_object import ListFineTuneEventsResponseObject
from .list_fine_tunes_response import ListFineTunesResponse
from .list_fine_tunes_response_object import ListFineTunesResponseObject
from .list_fine_tuning_job_events_response import ListFineTuningJobEventsResponse
from .list_fine_tuning_job_events_response_object import ListFineTuningJobEventsResponseObject
from .list_message_files_order import ListMessageFilesOrder
from .list_message_files_response import ListMessageFilesResponse
from .list_messages_order import ListMessagesOrder
from .list_messages_response import ListMessagesResponse
from .list_models_response import ListModelsResponse
from .list_models_response_object import ListModelsResponseObject
from .list_paginated_fine_tuning_jobs_response_object import ListPaginatedFineTuningJobsResponseObject
from .list_run_steps_order import ListRunStepsOrder
from .list_run_steps_response import ListRunStepsResponse
from .list_runs_order import ListRunsOrder
from .list_runs_response import ListRunsResponse
from .list_threads_response import ListThreadsResponse
from .message_creation import MessageCreation
from .message_creation_message_creation import MessageCreationMessageCreation
from .message_creation_type import MessageCreationType
from .message_files import MessageFiles
from .message_files_object import MessageFilesObject
from .model import Model
from .model_object import ModelObject
from .modify_assistant_request import ModifyAssistantRequest
from .modify_assistant_request_metadata import ModifyAssistantRequestMetadata
from .modify_message_request import ModifyMessageRequest
from .modify_message_request_metadata import ModifyMessageRequestMetadata
from .modify_run_request import ModifyRunRequest
from .modify_run_request_metadata import ModifyRunRequestMetadata
from .modify_thread_request import ModifyThreadRequest
from .modify_thread_request_metadata import ModifyThreadRequestMetadata
from .open_ai_file import OpenAIFile
from .open_ai_file_object import OpenAIFileObject
from .open_ai_file_purpose import OpenAIFilePurpose
from .open_ai_file_status import OpenAIFileStatus
from .retrieval_tool import RetrievalTool
from .retrieval_tool_call import RetrievalToolCall
from .retrieval_tool_call_retrieval import RetrievalToolCallRetrieval
from .retrieval_tool_call_type import RetrievalToolCallType
from .retrieval_tool_type import RetrievalToolType
from .run_steps import RunSteps
from .run_steps_last_error import RunStepsLastError
from .run_steps_last_error_code import RunStepsLastErrorCode
from .run_steps_metadata import RunStepsMetadata
from .run_steps_object import RunStepsObject
from .run_steps_status import RunStepsStatus
from .run_steps_type import RunStepsType
from .run_tool_call_object import RunToolCallObject
from .run_tool_call_object_function import RunToolCallObjectFunction
from .run_tool_call_object_type import RunToolCallObjectType
from .submit_tool_outputs_run_request import SubmitToolOutputsRunRequest
from .submit_tool_outputs_run_request_tool_outputs_item import SubmitToolOutputsRunRequestToolOutputsItem
from .system_message import SystemMessage
from .system_message_role import SystemMessageRole
from .text import Text
from .text_content_part import TextContentPart
from .text_content_part_type import TextContentPartType
from .text_text import TextText
from .text_type import TextType
from .the_message_object import TheMessageObject
from .the_message_object_metadata import TheMessageObjectMetadata
from .the_message_object_object import TheMessageObjectObject
from .the_message_object_role import TheMessageObjectRole
from .thread import Thread
from .thread_metadata import ThreadMetadata
from .thread_object import ThreadObject
from .tool_calls import ToolCalls
from .tool_calls_type import ToolCallsType
from .tool_message import ToolMessage
from .tool_message_role import ToolMessageRole
from .user_message import UserMessage
from .user_message_role import UserMessageRole

__all__ = (
    "ARunOnAThread",
    "ARunOnAThreadLastError",
    "ARunOnAThreadLastErrorCode",
    "ARunOnAThreadMetadata",
    "ARunOnAThreadObject",
    "ARunOnAThreadRequiredAction",
    "ARunOnAThreadRequiredActionSubmitToolOutputs",
    "ARunOnAThreadRequiredActionType",
    "ARunOnAThreadStatus",
    "Assistant",
    "AssistantFiles",
    "AssistantFilesObject",
    "AssistantMessage",
    "AssistantMessageFunctionCall",
    "AssistantMessageRole",
    "AssistantMetadata",
    "AssistantObject",
    "ChatCompletionFunctionCallOption",
    "ChatCompletionFunctions",
    "ChatCompletionMessageToolCall",
    "ChatCompletionMessageToolCallChunk",
    "ChatCompletionMessageToolCallChunkFunction",
    "ChatCompletionMessageToolCallChunkType",
    "ChatCompletionMessageToolCallFunction",
    "ChatCompletionMessageToolCallType",
    "ChatCompletionNamedToolChoice",
    "ChatCompletionNamedToolChoiceFunction",
    "ChatCompletionNamedToolChoiceType",
    "ChatCompletionResponseMessage",
    "ChatCompletionResponseMessageFunctionCall",
    "ChatCompletionResponseMessageRole",
    "ChatCompletionRole",
    "ChatCompletionStreamResponseDelta",
    "ChatCompletionStreamResponseDeltaFunctionCall",
    "ChatCompletionStreamResponseDeltaRole",
    "ChatCompletionTokenLogprob",
    "ChatCompletionTokenLogprobTopLogprobsItem",
    "ChatCompletionTool",
    "ChatCompletionToolChoiceOptionType0",
    "ChatCompletionToolType",
    "CodeInterpreterImageOutput",
    "CodeInterpreterImageOutputImage",
    "CodeInterpreterImageOutputType",
    "CodeInterpreterLogOutput",
    "CodeInterpreterLogOutputType",
    "CodeInterpreterTool",
    "CodeInterpreterToolCall",
    "CodeInterpreterToolCallCodeInterpreter",
    "CodeInterpreterToolCallType",
    "CodeInterpreterToolType",
    "CompletionUsage",
    "CreateAssistantFileRequest",
    "CreateAssistantRequest",
    "CreateAssistantRequestMetadata",
    "CreateChatCompletionFunctionResponse",
    "CreateChatCompletionFunctionResponseChoicesItem",
    "CreateChatCompletionFunctionResponseChoicesItemFinishReason",
    "CreateChatCompletionFunctionResponseObject",
    "CreateChatCompletionImageResponse",
    "CreateChatCompletionRequest",
    "CreateChatCompletionRequestFunctionCallType0",
    "CreateChatCompletionRequestLogitBias",
    "CreateChatCompletionRequestModelType1",
    "CreateChatCompletionRequestResponseFormat",
    "CreateChatCompletionRequestResponseFormatType",
    "CreateChatCompletionResponse",
    "CreateChatCompletionResponseChoicesItem",
    "CreateChatCompletionResponseChoicesItemFinishReason",
    "CreateChatCompletionResponseChoicesItemLogprobs",
    "CreateChatCompletionResponseObject",
    "CreateChatCompletionStreamResponse",
    "CreateChatCompletionStreamResponseChoicesItem",
    "CreateChatCompletionStreamResponseChoicesItemFinishReason",
    "CreateChatCompletionStreamResponseChoicesItemLogprobs",
    "CreateChatCompletionStreamResponseObject",
    "CreateCompletionRequest",
    "CreateCompletionRequestLogitBias",
    "CreateCompletionRequestModelType1",
    "CreateCompletionResponse",
    "CreateCompletionResponseChoicesItem",
    "CreateCompletionResponseChoicesItemFinishReason",
    "CreateCompletionResponseChoicesItemLogprobs",
    "CreateCompletionResponseChoicesItemLogprobsTopLogprobsItem",
    "CreateCompletionResponseObject",
    "CreateEditRequest",
    "CreateEditRequestModelType1",
    "CreateEmbeddingRequest",
    "CreateEmbeddingRequestEncodingFormat",
    "CreateEmbeddingRequestModelType1",
    "CreateEmbeddingResponse",
    "CreateEmbeddingResponseObject",
    "CreateEmbeddingResponseUsage",
    "CreateFileRequest",
    "CreateFileRequestPurpose",
    "CreateImageEditRequest",
    "CreateImageEditRequestModelType1",
    "CreateImageEditRequestResponseFormat",
    "CreateImageEditRequestSize",
    "CreateImageRequest",
    "CreateImageRequestModelType1",
    "CreateImageRequestQuality",
    "CreateImageRequestResponseFormat",
    "CreateImageRequestSize",
    "CreateImageRequestStyle",
    "CreateImageVariationRequest",
    "CreateImageVariationRequestModelType1",
    "CreateImageVariationRequestResponseFormat",
    "CreateImageVariationRequestSize",
    "CreateMessageRequest",
    "CreateMessageRequestMetadata",
    "CreateMessageRequestRole",
    "CreateModerationRequest",
    "CreateModerationRequestModelType1",
    "CreateModerationResponse",
    "CreateModerationResponseResultsItem",
    "CreateModerationResponseResultsItemCategories",
    "CreateModerationResponseResultsItemCategoryScores",
    "CreateRunRequest",
    "CreateRunRequestMetadata",
    "CreateSpeechRequest",
    "CreateSpeechRequestModelType1",
    "CreateSpeechRequestResponseFormat",
    "CreateSpeechRequestVoice",
    "CreateThreadAndRunRequest",
    "CreateThreadAndRunRequestMetadata",
    "CreateThreadRequest",
    "CreateThreadRequestMetadata",
    "CreateTranscriptionRequest",
    "CreateTranscriptionRequestModelType1",
    "CreateTranscriptionRequestResponseFormat",
    "CreateTranscriptionResponse",
    "CreateTranslationRequest",
    "CreateTranslationRequestModelType1",
    "CreateTranslationResponse",
    "DeleteAssistantFileResponse",
    "DeleteAssistantFileResponseObject",
    "DeleteAssistantResponse",
    "DeleteAssistantResponseObject",
    "DeleteFileResponse",
    "DeleteFileResponseObject",
    "DeleteMessageResponse",
    "DeleteMessageResponseObject",
    "DeleteModelResponse",
    "DeleteThreadResponse",
    "DeleteThreadResponseObject",
    "Edit",
    "EditChoicesItem",
    "EditChoicesItemFinishReason",
    "EditObject",
    "Embedding",
    "EmbeddingObject",
    "Error",
    "ErrorResponse",
    "FileCitation",
    "FileCitationFileCitation",
    "FileCitationType",
    "FilePath",
    "FilePathFilePath",
    "FilePathType",
    "FineTune",
    "FineTuneEvent",
    "FineTuneEventObject",
    "FineTuneHyperparams",
    "FineTuneObject",
    "FineTuningJobEvent",
    "FineTuningJobEventLevel",
    "FineTuningJobEventObject",
    "FunctionMessage",
    "FunctionMessageRole",
    "FunctionObject",
    "FunctionParameters",
    "FunctionTool",
    "FunctionToolCall",
    "FunctionToolCallFunction",
    "FunctionToolCallType",
    "FunctionToolType",
    "Image",
    "ImageContentPart",
    "ImageContentPartImageUrl",
    "ImageContentPartImageUrlDetail",
    "ImageContentPartType",
    "ImageFile",
    "ImageFileImageFile",
    "ImageFileType",
    "ImagesResponse",
    "ListAssistantFilesOrder",
    "ListAssistantFilesResponse",
    "ListAssistantsOrder",
    "ListAssistantsResponse",
    "ListFilesResponse",
    "ListFilesResponseObject",
    "ListFineTuneEventsResponse",
    "ListFineTuneEventsResponseObject",
    "ListFineTunesResponse",
    "ListFineTunesResponseObject",
    "ListFineTuningJobEventsResponse",
    "ListFineTuningJobEventsResponseObject",
    "ListMessageFilesOrder",
    "ListMessageFilesResponse",
    "ListMessagesOrder",
    "ListMessagesResponse",
    "ListModelsResponse",
    "ListModelsResponseObject",
    "ListPaginatedFineTuningJobsResponseObject",
    "ListRunsOrder",
    "ListRunsResponse",
    "ListRunStepsOrder",
    "ListRunStepsResponse",
    "ListThreadsResponse",
    "MessageCreation",
    "MessageCreationMessageCreation",
    "MessageCreationType",
    "MessageFiles",
    "MessageFilesObject",
    "Model",
    "ModelObject",
    "ModifyAssistantRequest",
    "ModifyAssistantRequestMetadata",
    "ModifyMessageRequest",
    "ModifyMessageRequestMetadata",
    "ModifyRunRequest",
    "ModifyRunRequestMetadata",
    "ModifyThreadRequest",
    "ModifyThreadRequestMetadata",
    "OpenAIFile",
    "OpenAIFileObject",
    "OpenAIFilePurpose",
    "OpenAIFileStatus",
    "RetrievalTool",
    "RetrievalToolCall",
    "RetrievalToolCallRetrieval",
    "RetrievalToolCallType",
    "RetrievalToolType",
    "RunSteps",
    "RunStepsLastError",
    "RunStepsLastErrorCode",
    "RunStepsMetadata",
    "RunStepsObject",
    "RunStepsStatus",
    "RunStepsType",
    "RunToolCallObject",
    "RunToolCallObjectFunction",
    "RunToolCallObjectType",
    "SubmitToolOutputsRunRequest",
    "SubmitToolOutputsRunRequestToolOutputsItem",
    "SystemMessage",
    "SystemMessageRole",
    "Text",
    "TextContentPart",
    "TextContentPartType",
    "TextText",
    "TextType",
    "TheMessageObject",
    "TheMessageObjectMetadata",
    "TheMessageObjectObject",
    "TheMessageObjectRole",
    "Thread",
    "ThreadMetadata",
    "ThreadObject",
    "ToolCalls",
    "ToolCallsType",
    "ToolMessage",
    "ToolMessageRole",
    "UserMessage",
    "UserMessageRole",
)
