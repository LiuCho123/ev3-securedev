from flask import Flask, request, make_response
from markupsafe import escape
from prometheus_client import start_http_server, Summary

app = Flask(__name__)
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/hello')
@REQUEST_TIME.time()
def hello():
    name = escape(request.args.get('name', 'Mundo'))
    response = make_response(f"Hello, {name}!")
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000, debug=False)