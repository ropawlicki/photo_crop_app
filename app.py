from flask import Flask  # type: ignore[import]
from routes import main, photos

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(photos)

if __name__ == "__main__":
    app.run(debug=True)
