import os
from flask import Flask
import requests


app = Flask(__name__)

FIREBASE_SERVER_KEY=''
FIREBASE_URL='https://fcm.googleapis.com/fcm/send'
URL_TEST='https://httpbin.org/post'


@app.route('/')
@app.route('/index')
def hello_world():
    return 'hello world!'


# registrar usuario no firebase (um id e device_id)
@app.route('/register', methods=['POST'])
def register():
    return 'register!'


# enviar push a um device_id (receber o id do usuario e o conteudo do push / buscar o deviceid no firebase)
@app.route('/send', methods=['POST'])
def send():
    return 'send!'


@app.route('/send/<string:deviceid>', methods=['POST'])
def send_push(deviceid):
    headers = {'Content-Type': 'application/json', 'Authorization': FIREBASE_SERVER_KEY}
    data = {"notification": {"title": "Titulo teste 5", "body": "Body teste!", "click_action": "http://localhost:4200/signup", "icon": "https://placeimg.com/128/128/people"},"to": deviceid}
    response = requests.post(FIREBASE_URL, headers=headers, json=data)
    json_response = response.json()
    return json_response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='localhost', port=port)
