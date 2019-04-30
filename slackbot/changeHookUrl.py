from flask import Flask, jsonify, request, Response
import requests
app = Flask(__name__)

@app.route('/webhooks/slack/webhook', methods=["POST"])
def events():
    return request.json.get("challenge")