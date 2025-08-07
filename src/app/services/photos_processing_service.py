from typing import List
from app.schemas.photos import ProcessedFileDict
from werkzeug.datastructures import FileStorage, MultiDict


class PhotosProcessingService:
    def __init__(self, files: MultiDict[str, FileStorage]):
        self.files: MultiDict[str, FileStorage] = files
        self.processed_files: List[ProcessedFileDict] = []

    def __call__(self) -> None:
        for key, files in self.files.lists():
            for file in files:
                file_dict: ProcessedFileDict = {
                    "io": file.stream,
                    "filename": file.filename,
                }
                self.processed_files.append(file_dict)
