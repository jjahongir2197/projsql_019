from flask import Flask, request

app = Flask(__name__)

requests_count = {}

@app.route('/api')
def api():
    ip = request.remote_addr

    if ip not in requests_count:
        requests_count[ip] = 0

    requests_count[ip] += 1

    if requests_count[ip] > 5:
        return "Too many requests"

    return "Success"
