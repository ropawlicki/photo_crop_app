from io import BytesIO
from zipfile import ZipFile
from typing import List
from app.schemas.photos import ProcessedFileDict


class ZipFilesService:
    def __init__(self, files_dict: List[ProcessedFileDict]):
        self.files_dict: List[ProcessedFileDict] = files_dict
        self.zip_buffer: BytesIO = BytesIO()

    def __call__(self) -> BytesIO:
        with ZipFile(self.zip_buffer, "w") as zip_file:
            for file_dict in self.files_dict:
                file_dict["io"].seek(0)
                zip_file.writestr(file_dict["filename"], file_dict["io"].read())
        self.zip_buffer.seek(0)
        return self.zip_buffer
