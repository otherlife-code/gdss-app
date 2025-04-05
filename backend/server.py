
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)

@app.route('/api/save', methods=['POST'])
def save_data():
    data = request.get_json()
    conn = sqlite3.connect('gdss.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS decisions (id INTEGER PRIMARY KEY AUTOINCREMENT, users TEXT, weights TEXT, total_scores TEXT)")
    c.execute("INSERT INTO decisions (users, weights, total_scores) VALUES (?, ?, ?)",
              (json.dumps(data['users']), json.dumps(data['weights']), json.dumps(data['totalScores'])))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'}), 200

if __name__ == '__main__':
    app.run(debug=True)
