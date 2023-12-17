from enum import Enum


class CreateCompletionRequestModelType1(str, Enum):
    BABBAGE_002 = "babbage-002"
    CODE_DAVINCI_002 = "code-davinci-002"
    DAVINCI_002 = "davinci-002"
    GPT_3_5_TURBO_INSTRUCT = "gpt-3.5-turbo-instruct"
    TEXT_ADA_001 = "text-ada-001"
    TEXT_BABBAGE_001 = "text-babbage-001"
    TEXT_CURIE_001 = "text-curie-001"
    TEXT_DAVINCI_001 = "text-davinci-001"
    TEXT_DAVINCI_002 = "text-davinci-002"
    TEXT_DAVINCI_003 = "text-davinci-003"

    def __str__(self) -> str:
        return str(self.value)
