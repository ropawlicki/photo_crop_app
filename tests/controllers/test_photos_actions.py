from app.controllers.photos_actions import crop_photos
from tests.factories.file_factory import FileFactory
from werkzeug.datastructures import MultiDict
import pytest
import io


@pytest.fixture
def files():
    return MultiDict({"photos": []})


@pytest.fixture
def mock_photos_service(mocker):
    mock = mocker.patch("app.controllers.photos_actions.PhotosProcessingService")
    mock.return_value.processed_files = [
        FileFactory(filename="test_file_1.jpg"),
        FileFactory(filename="test_file_2.jpg"),
    ]
    return mock


@pytest.fixture
def mock_zip_service(mocker):
    mock = mocker.patch("app.controllers.photos_actions.ZipFilesService")
    mock.return_value.return_value = io.BytesIO(b"dummy zip content")
    return mock


def test_crop_photos_returns_zip_response(files, mock_photos_service, mock_zip_service):
    response = crop_photos(files)
    assert response.mimetype == "application/zip"


def test_crop_photos_passes_files_to_processing_service(mock_photos_service, mock_zip_service):
    crop_photos(files)
    mock_photos_service.assert_called_once_with(files)


def test_crop_photos_passes_files_from_processing_service_to_zip_service(files, mock_photos_service, mock_zip_service):
    crop_photos(files)
    mock_zip_service.assert_called_once_with(mock_photos_service.return_value.processed_files)
