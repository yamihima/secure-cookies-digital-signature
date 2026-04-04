
from flask import Flask, request, make_response, redirect
import hmac
import hashlib
import time
import base64
import json

app = Flask(__name__)

SECRET_KEY = b'super_secret_server_key'

def create_mac(data):
    return hmac.new(SECRET_KEY, data.encode(), hashlib.sha256).hexdigest()

def verify_mac(data, mac):
    expected = create_mac(data)
    return hmac.compare_digest(expected, mac)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        role = "user"
        expiration = str(int(time.time()) + 300)

        payload = json.dumps({
            "username": username,
            "role": role,
            "exp": expiration
        })

        mac = create_mac(payload)

        response = make_response(redirect('/protected'))
        response.set_cookie('payload', base64.b64encode(payload.encode()).decode())
        response.set_cookie('mac', mac)

        return response

    return '''
    <form method="post">
    Username: <input name="username"><br>
    <input type="submit">
    </form>
    '''

@app.route('/protected')
def protected():
    payload = request.cookies.get('payload')
    mac = request.cookies.get('mac')

    if not payload or not mac:
        return "No cookie found"

    payload = base64.b64decode(payload).decode()

    if not verify_mac(payload, mac):
        return "Tampering detected!"

    return "Access granted: " + payload

app.run(host='0.0.0.0', port=5000)

