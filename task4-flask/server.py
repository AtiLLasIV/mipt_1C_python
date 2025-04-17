from flask import Flask, jsonify, request, Response
from dotenv import dotenv_values
from controllers import operation

app = Flask(__name__)


@app.route("/")
def server_info() -> str:
    return "My server"


@app.route("/author")
def author() -> Response:
    author = {
        "name": "Stas",
        "course": 3,
        "age": 21,
    }
    return jsonify(author)


def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return config["PORT"]
    return 5000


@app.route("/sum")
def runner() -> Response:
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'sum': operation(a, b)})


if __name__ == "__main__":
    app.run(debug=True, port=get_port())
