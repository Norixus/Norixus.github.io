from flask import Flask, request

app = Flask(__name__)

webhook_secret = 'your_secret'

@app.route('/handle_webhook', methods=['POST'])
def handle_webhook():
    if request.headers.get('trello-webhook-secret') == webhook_secret:
        # do something with the data from the webhook event
        print(request.json)
        return 'Webhook event received', 200
    else:
        return 'Unauthorized', 401


@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
