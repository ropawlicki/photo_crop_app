import pytest
from app.services.zip_files_service import ZipFilesService
from tests.factories.file_factory import FileFactory
from zipfile import ZipFile


@pytest.fixture
def files_dict():
    return [
        {"filename": "test1.jpg", "io": FileFactory(filename="test1.jpg").stream},
        {"filename": "test2.jpg", "io": FileFactory(filename="test2.jpg").stream},
    ]


def test_zip_files_service_creates_zip_from_files_dict(files_dict):
    service = ZipFilesService(files_dict)
    zip_buffer = service()

    with ZipFile(zip_buffer) as zip_file:
        for file_dict in files_dict:
            assert file_dict["filename"] in zip_file.namelist()
            with zip_file.open(file_dict["filename"]) as zip_file_stream:
                file_dict["io"].seek(0)
                assert zip_file_stream.read() == file_dict["io"].read()
