from flask import Blueprint, request  # type: ignore[import]
from werkzeug.datastructures import MultiDict, FileStorage  # type: ignore[import]
from app.controllers.photos_actions import crop_photos

main = Blueprint("main", __name__, url_prefix="/")
photos = Blueprint("photos", __name__, url_prefix="/photos")


@main.route("/")
def healthcheck() -> tuple[str, int]:
    return "App is running!", 200


@photos.route("/crop", methods=["POST"])
def crop_photos_route() -> object:
    files: MultiDict[str, FileStorage] = request.files
    return crop_photos(files)
