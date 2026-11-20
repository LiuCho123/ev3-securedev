from flask import Flask, request, make_response
from markupsafe import escape

app = Flask(__name__)

@app.route('/hello')
def hello():
    name = escape(request.args.get('name', 'Mundo'))
    response = make_response(f"Hello, {name}!")
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)