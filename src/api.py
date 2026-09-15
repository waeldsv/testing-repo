from flask import Flask , request

app = Flask(__name__)


@app.get("/hello")
def hello():
    name = request.args.get("name", "World")
    return f"Hello {name}"

