from flask import Flask, request, jsonify
from kanpo import normalized_kampo_data  # kanpo.py からデータを読み込む

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "漢方API（Flask版）が動作しています！"})

@app.route('/search', methods=['GET'])
def search_kampo():
    numbers = request.args.getlist('numbers')
    result = {}

    for num in numbers:
        normalized_num = str(int(num))  # "001" → "1" に変換
        if normalized_num in normalized_kampo_data:
            for ingredient, amount in normalized_kampo_data[normalized_num].items():
                result[ingredient] = result.get(ingredient, 0) + amount

    return jsonify({"total_ingredients": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
