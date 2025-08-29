from urllib import request

from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/webhook", methods=["post"])
def webhook():
    if request.method == 'POST':
        print(request.json)
        return "Success", 200
    else:
        abort(400)

if __name__ == "__main__":
    app.run()