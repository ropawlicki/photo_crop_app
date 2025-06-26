from flask import Blueprint, request  # type: ignore[import]
from photos_actions import crop_photos

main = Blueprint("main", __name__, url_prefix="/")
photos = Blueprint("photos", __name__, url_prefix="/photos")


@main.route("/")
def healthcheck():
    return "App is running!", 200


@photos.route("/crop", methods=["POST"])
def crop_photos_route():
    files = request.files
    return crop_photos(files)
