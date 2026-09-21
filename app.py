import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    greeting = os.environ.get("GREETING", "Hello from the cloud!")
    return (
        '<body style="background-color: yellow;">'
        f"<p>{greeting}</p>"
        "<p>App developed by Pijus</p>"
        "<p>Please use responsibly</p>"
        "</body>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
