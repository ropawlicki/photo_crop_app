from typing import IO, TypedDict

class ProcessedFileDict(TypedDict):
    io: IO
    filename: str
