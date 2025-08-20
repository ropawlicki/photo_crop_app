from typing import List
from app.schemas.photos import ProcessedFileDict
from app.services.cropping.cropping_service_base import CroppingService
from app.services.cropping.vips_cropping_service import VipsCroppingService
from werkzeug.datastructures import FileStorage, MultiDict


class PhotosProcessingService:
    def __init__(self, files: MultiDict[str, FileStorage]):
        self.files: MultiDict[str, FileStorage] = files
        self.processed_files: List[ProcessedFileDict] = []

    def __call__(self) -> None:
        for key, files in self.files.lists():
            for file in files:
                cropping_service = self._initialize_cropping_service(file)
                cropping_service()
                file_dict: ProcessedFileDict = {
                    "io": cropping_service.cropped_image_stream,
                    "filename": file.filename if file.filename is not None else "",
                }
                self.processed_files.append(file_dict)

    def _initialize_cropping_service(self, file) -> CroppingService:
        return VipsCroppingService(file)
