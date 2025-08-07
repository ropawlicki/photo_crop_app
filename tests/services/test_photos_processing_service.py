from app.services.photos_processing_service import PhotosProcessingService
from tests.factories.file_factory import FileFactory
from werkzeug.datastructures import MultiDict


def test_processed_file_name_match_input():
    filenames = ["test1.jpg", "test2.jpg"]
    files = [FileFactory(filename=name) for name in filenames]
    multidict = MultiDict({"images": files})
    service = PhotosProcessingService(multidict)
    service()

    processed = service.processed_files
    assert [f["filename"] for f in processed] == filenames
