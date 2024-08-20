from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Добавляем поддержку CORS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save_result', methods=['POST'])
def save_result():
    data = request.json
    # Логика сохранения результатов в базу данных или файл
    return jsonify({"status": "success"})

@app.route('/get_results')
def get_results():
    # Логика получения результатов из базы данных или файла
    results = []  # Пример списка результатов
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
