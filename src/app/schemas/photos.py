from typing import IO, TypedDict


class ProcessedFileDict(TypedDict):
    io: IO[bytes]
    filename: str
