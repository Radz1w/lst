from flask import Flask, jsonify
import redis
import os
app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_client = redis.Redis(host=redis_host, port=6379, decode_responses=True)
@app.route('/ping')
def ping():
    return jsonify({"status": "ok"})
@app.route('/count')
def count():
    visits = redis_client.incr('counter')
    return jsonify({visits: visits})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
