import requests
import re
import random
from bs4 import BeautifulSoup
from collections import defaultdict
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
line_bot_api = LineBotApi('yCn4BcbCUWrYQ+7yj/IaYhDrSyXh5djYTH6lYbwhVJyRfbBSxz+/DJi3+ewn3TXIvWMaJgfi1vGLTeywqwOBdDI5zYFTzX+78BxrKvBM4MA8pkyFZA7s8ha0j3ANroDQHIyQ3vWNCypVivJL5QBESAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('55c07c36c8dd78f272e490be1e3f9706')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == '__main__':
    app.run()
