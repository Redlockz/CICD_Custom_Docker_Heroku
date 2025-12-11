"""
Simple Python Flask Web Application
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    """Home endpoint"""
    return jsonify({
        'message': 'Hello from Dockerized Flask App!',
        'status': 'running',
        'version': '1.0.0'
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'flask-app'
    }), 200


@app.route('/api/info')
def info():
    """Info endpoint"""
    return jsonify({
        'app': 'Flask Docker App',
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'port': os.getenv('PORT', '5000')
    })


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
