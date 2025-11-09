from flask import Flask, request, jsonify
from flask_cors import CORS
from main import main_chain

app = Flask(__name__)
CORS(app)

@app.route("/ask", methods=["POST"])
def ask_question():
    try:
        data = request.get_json()
        video_id = data.get("video_id")
        question = data.get("question")

        if not video_id or not question:
            return jsonify({"error": "Missing video_id or question"}), 400

        print(f"🧠 Received → video_id={video_id}, question={question}")
        answer = main_chain(video_id, question)
        return jsonify({"answer": answer})
    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
