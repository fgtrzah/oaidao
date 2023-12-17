from enum import Enum


class CreateSpeechRequestResponseFormat(str, Enum):
    AAC = "aac"
    FLAC = "flac"
    MP3 = "mp3"
    OPUS = "opus"

    def __str__(self) -> str:
        return str(self.value)
