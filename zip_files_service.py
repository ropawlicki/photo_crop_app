from io import BytesIO
from zipfile import ZipFile


class ZipFilesService:
    def __init__(self, files_dict):
        self.files_dict = files_dict
        self.zip_buffer = BytesIO()

    def __call__(self):
        with ZipFile(self.zip_buffer, "w") as zip_file:
            for file_dict in self.files_dict:
                file_dict["io"].seek(0)
                zip_file.writestr(file_dict["filename"], file_dict["io"].read())
        self.zip_buffer.seek(0)
        return self.zip_buffer
