from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def hello_world(a: int):
    return str(a)

@app.route('/process_list', methods=['POST'])
def process_list():
    data = request.get_json() # 固定写法

    task_id = data["task_id"]
    method_name = data["method_name"]
    print(f"task_id: {task_id}, method_name: {method_name}")
    return f"task_id: {task_id}, method_name: {method_name}"



@app.route('/config/methodList')
def a():
    return json.dumps(['a','b'])

if __name__ == '__main__':
    app.run()
