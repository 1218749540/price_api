from flask import Flask, request, jsonify
from scraper import get_price_history

app = Flask(__name__)

@app.route('/price', methods=['GET'])
def price():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "请提供商品链接"}), 400

    try:
        price_data = get_price_history(url)
        return jsonify(price_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
