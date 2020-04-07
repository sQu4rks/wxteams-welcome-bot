""" A simple welcome bot for Webex Teams using the webexteamssdk to show
how easy it is to create customized bots that react to user joining a
space.
"""
import os
import sys

from flask import Flask, request, jsonify
from webexteamssdk import WebexTeamsAPI, Webhook

from pyadaptivecards.card import AdaptiveCard
from pyadaptivecards.components import TextBlock, Image

api = WebexTeamsAPI()
app = Flask(__name__)

MESSAGE = """
Welcome 👋🏻 {name} to the Ambassadors. We want to share a few house rules and program updates!
House Rules 📜
💬 Before asking questions in a space, please check Google or specifically the [Collaboration Help Portal](http://help.webex.com/).
❓If you can’t find your answer, post your question in the appropriate community space. Learn about these spaces [here](https://ambassador.webex.com/webex-teams-communities/).
👊🏻 Adhere to the Community [Code of Conduct](https://ambassador.webex.com/code-of-conduct/).
🙊 The Code of Conduct includes rules of not using the @all command, creating new Spaces, adding bots and users to the Spaces.
"""

def make_card(name):
    card_body = []

    logo = Image("https://gist.githubusercontent.com/sQu4rks/82ce8e2f0aa9f37413b7913fc1c0487b/raw/3152f2158c8b99e114ae0803a921b1ff26c15709/welcome-banner.jpg")
    card_body.append(logo)

    greeting = TextBlock(MESSAGE.format(name=name))
    card_body.append(greeting)

    card = AdaptiveCard(body=card_body)

    attachment = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": card.to_dict(),
    }

    return attachment

@app.route('/alive')
def alive():
    return "I am up!"


@app.route("/webhook/membership", methods=['POST'])
def webhook_membership():
    raw_json = request.get_json()

    member_name = raw_json['data']['personDisplayName']
    member_id = raw_json['data']['personId']
    space = api.rooms.get(raw_json['data']['roomId'])

    if space.type == "group":
        fmt_msg = MESSAGE.format(name=member_name, event_space=space.title)

        if not api.people.me().id == raw_json['data']['personId']:
            api.messages.create(toPersonEmail=raw_json['data']['personEmail'], markdown=fmt_msg, attachments=[make_card(member_name)])

    return jsonify({"success": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8010, debug=True)
