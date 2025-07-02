import io
from werkzeug.datastructures import FileStorage, MultiDict
from app.services.photos_processing_service import PhotosProcessingService


class DummyFile:
    def __init__(self, filename, content):
        self.filename = filename
        self.stream = io.BytesIO(content)


def test_photos_processing_service_single_file():
    file = DummyFile("test.jpg", b"fake image data")
    files = MultiDict([("photos", [file])])
    service = PhotosProcessingService(files)
    service()
    assert len(service.processed_files) == 1
    assert service.processed_files[0]["filename"] == "test.jpg"
    assert service.processed_files[0]["io"].read() == b"fake image data"


def test_photos_processing_service_multiple_files():
    file1 = DummyFile("a.jpg", b"a")
    file2 = DummyFile("b.jpg", b"b")
    files = MultiDict([("photos", [file1, file2])])
    service = PhotosProcessingService(files)
    service()
    assert len(service.processed_files) == 2
    filenames = {f["filename"] for f in service.processed_files}
    assert filenames == {"a.jpg", "b.jpg"}
