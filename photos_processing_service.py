from typing import Any, List, TypedDict, IO
from werkzeug.datastructures import FileStorage, MultiDict  # type: ignore[import]


class PhotosProcessingService:
    def __init__(self, files: Any):
        self.files: MultiDict[str, FileStorage] = files
        self.processed_files: List[ProcessedFileDict] = []

    def __call__(self) -> None:
        import pdb

        for key, files in self.files.lists():
            for file in files:
                file_dict: ProcessedFileDict = {
                    "io": file.stream,
                    "filename": file.filename,
                }
                self.processed_files.append(file_dict)


class ProcessedFileDict(TypedDict):
    io: IO
    filename: str
