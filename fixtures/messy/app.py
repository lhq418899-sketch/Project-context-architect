"""Web view (stub). Intended to wrap CLI output; not yet implemented."""

from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def index() -> Response:
    return Response("stub: dashboard not implemented", status=501)
