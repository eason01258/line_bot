from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi('g+JL4vB5TakY/mnNV7vom5FsnVn0gqzxRZ8XJIfxnsrpGD3+mKeVcTYf9LLUkxyNe92MY8AnrTGxq4TXcNfsuhiifuFv8qSmydGIIRrHYDN+YQOZoYAVhj/p50lu4AB8SZ2348CfGL+NQ0to4ddtkAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('be89637c3bfc459e2d9367bd049a5414')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    if msg == '交互作用' :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='請輸入藥品1'))

    elif msg in ['安安','你好','妳好','hi','Hi'] :
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='哩賀'))

    elif msg == '貼圖':
        line_bot_api.reply_message(
            event.reply_token,
            StickerSendMessage(
            package_id='1',
            sticker_id='1'))

    # drug_1 = event.message.text
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text='請輸入藥品2'))

    # drug_2 = event.message.text
    #     opt = f'查詢藥品為{drug_1}與{drug_2}'
    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=opt))
    else :
        line_bot_api.reply_message(
         event.reply_token,
         TextSendMessage(text='無效指令'))







if __name__ == "__main__":
    app.run()