from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask API is running! Use POST /procesar to process text."

@app.route('/procesar', methods=['POST'])
def procesar():
    t = request.json.get('text', '')
    z = re.search(r'(Makati|BGC|Ortigas)', t, re.I)
    c = re.search(r'(\d+)\s*cuartos?', t, re.I)
    p = re.search(r'₱?\s*([\d,]+)', t)
    return jsonify({
        "zona": z.group(1) if z else None,
        "cuartos": int(c.group(1)) if c else None,
        "precio": int(p.group(1).replace(',', '')) if p else None
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)