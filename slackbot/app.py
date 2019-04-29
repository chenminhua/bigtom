from flask import Flask, jsonify, request, Response
import requests
app = Flask(__name__)

@app.route('/', methods=["POST"])
def events():
  event = request.json.get('event')
  event_type = event.get("type")
  if (event_type == "app_mention"):
    requests.post("https://slack.com/api/chat.postMessage",
    json={
      "text": "hello world",
      "channel": event.get("channel")
    },
    headers={
      "Content-type": "application/json",
      "Authorization": "Bearer xoxb-609516301041-614658922113-42kiT58gDPt31Vi2LFldWIBt"
    })

  return Response("OK", status = 200)