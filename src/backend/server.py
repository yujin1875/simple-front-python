"""
이 서버의 목적

- POST 요청을 받는다
- request.body(JSON)를 그대로 받는다
- id: 101 을 강제로 추가한다
- 마치 데이터가 새롭게 추가된 것처럼, 가짜 응답값을 꾸며서 뱉어준다
"""

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# -----------------------------
# CORS 설정 (모든 출처 허용)
# -----------------------------
CORS(app)

@app.route("/posts", methods=["POST"])
def create_post():
    # -----------------------------
    # 1️⃣ 요청 body(JSON) 받기
    # -----------------------------
    data = request.get_json()

    # -----------------------------
    # 2️⃣ mock 동작
    # -----------------------------
    # 실제 DB 저장 ❌
    # 실제 로직 ❌
    # 그냥 id: 101만 추가
    data["id"] = 101

    # -----------------------------
    # 3️⃣ 그대로 응답
    # -----------------------------
    return jsonify(data), 201

@app.route("/hello", methods=["GET"])
def hello():
    return "너부리야~", 200

if __name__ == "__main__":
    app.run(debug=True)
