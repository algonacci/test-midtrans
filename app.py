import time

import midtransclient
from dotenv import dotenv_values
from flask import Flask, jsonify, render_template, request

config = dotenv_values(".env")
order_id = str(int(time.time() * 1000000))


app = Flask(__name__)
MIDTRANS_SERVER_KEY = config["MIDTRANS_SERVER_KEY"]
MIDTRANS_CLIENT_KEY = config["MIDTRANS_CLIENT_KEY"]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        price = request.form["price"]
        snap = midtransclient.Snap(
            is_production=False,
            server_key=MIDTRANS_SERVER_KEY,
            client_key=MIDTRANS_CLIENT_KEY,
        )
        param = {
            "transaction_details": {
                "order_id": "test-transaction-{}".format(order_id),
                "gross_amount": price
            }, "credit_card": {
                "secure": True
            }
        }
        transaction = snap.create_transaction(param)
        transaction_token = transaction['token']
        print(transaction_token)
        return jsonify({
            "token": transaction_token,
        }), 200
    else:
        return render_template("index.html")


@app.route("/pay", methods=["POST"])
def pay():
    if request.method == "POST":
        price = request.form["price"]
        snap = midtransclient.Snap(
            is_production=False,
            server_key=MIDTRANS_SERVER_KEY,
            client_key=MIDTRANS_CLIENT_KEY,
        )
        param = {
            "transaction_details": {
                "order_id": "test-transaction-{}".format(order_id),
                "gross_amount": price
            }, "credit_card": {
                "secure": True
            }
        }
        transaction = snap.create_transaction(param)
        transaction_token = transaction['token']
        print(transaction_token)
        return jsonify({
            "token_url": "https://app.sandbox.midtrans.com/snap/v2/vtweb/" + transaction_token,
            "token":  transaction_token,
        }), 200
    else:
        return jsonify({
            "status": {
                "code": 403,
                "message": "USE POST METHOD!"
            }
        }), 403


if __name__ == "__main__":
    app.run()
