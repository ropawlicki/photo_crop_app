from flask import send_file, Response
from werkzeug.datastructures import MultiDict, FileStorage
from app.services.photos_processing_service import PhotosProcessingService
from app.services.zip_files_service import ZipFilesService


def crop_photos(files: MultiDict[str, FileStorage]) -> Response:
    processing_service = PhotosProcessingService(files)
    processing_service()
    processed_files = processing_service.processed_files

    zip_service = ZipFilesService(processed_files)
    zip_buffer = zip_service()

    return send_file(
        zip_buffer,
        mimetype="application/zip",
        as_attachment=True,
        download_name="cropped_photos.zip",
    )
