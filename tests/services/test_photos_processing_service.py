import pytest
from app.services.photos_processing_service import PhotosProcessingService
from tests.factories.file_factory import FileFactory
from unittest.mock import MagicMock, patch
from werkzeug.datastructures import MultiDict


@pytest.fixture
def mock_cropping_service():
    mock_service = MagicMock()
    mock_service.return_value.cropped_image_stream = b"fake-bytes"
    with patch("app.services.photos_processing_service.VipsCroppingService", mock_service):
        yield mock_service


def test_processed_file_name_match_input(mock_cropping_service):
    filenames = ["test1.jpg", "test2.jpg"]
    files = [FileFactory(filename=name) for name in filenames]
    multidict = MultiDict({"images": files})
    service = PhotosProcessingService(multidict)
    service()

    processed = service.processed_files
    assert [f["filename"] for f in processed] == filenames
