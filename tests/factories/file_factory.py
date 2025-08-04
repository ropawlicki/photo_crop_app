import io
import factory
from werkzeug.datastructures import FileStorage


class FileFactory(factory.Factory):
    class Meta:
        model = FileStorage

    filename = factory.Faker("file_name", extension="jpg")
    content = factory.Faker("binary", length=16)

    @classmethod
    def _create(cls, model_class, **kwargs):
        filename = kwargs.get("filename") or cls.filename.generate({})
        content = kwargs.get("content") or cls.content.generate({})
        return FileStorage(stream=io.BytesIO(content), filename=filename)
