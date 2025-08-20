from abc import ABC, abstractmethod
from typing import IO


class CroppingService(ABC):
    @abstractmethod
    def __init__(self, image_stream: IO[bytes], **kwargs):
        pass

    @abstractmethod
    def __call__(self) -> bool:
        pass

    @property
    @abstractmethod
    def cropped_image_stream(self) -> IO[bytes]:
        pass
