from flask import Flask, render_template, request, jsonify
import requests
import json
import os

app = Flask(__name__)

# 🧠 Đọc dữ liệu từ file JSON
def load_menu():
    with open(os.path.join("data", "menu.json"), "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    api_key = "AIzaSyDRlaN1tzTpUXfMW115uRRUY15mSeVEN2M"  # 🔑 API key của bạn

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

    # 📋 Đọc menu
    MENU = load_menu()
    menu_text = "\n".join(
        [f"- {item['name']} ({item['type']}, {item['taste']}, {item['temperature']}, giá {item['price']})"
         for item in MENU]
    )

    # 💡 Prompt nâng cấp: có nhận dạng ý định
    system_prompt = (
        "Bạn là AI Barista thân thiện của quán cà phê ☕.\n"
        "Nhiệm vụ: Gợi ý 1–2 món trong menu phù hợp với ý định hoặc cảm xúc của khách.\n\n"
        "Trước tiên, hãy phân tích nội dung khách nói để hiểu họ muốn gì:\n"
        "- Nếu khách nói 'trời nóng', 'muốn giải khát' → gợi ý đồ lạnh.\n"
        "- Nếu khách nói 'buồn ngủ', 'mệt', 'cần tỉnh táo' → gợi ý cà phê mạnh.\n"
        "- Nếu khách nói 'thích ngọt', 'thèm sữa', 'muốn béo' → gợi ý đồ sữa hoặc sinh tố.\n"
        "- Nếu khách nói 'không uống được cà phê' → gợi ý trà hoặc sinh tố.\n"
        "- Nếu khách hỏi món không có trong menu → gợi ý món tương tự.\n\n"
        f"📜 MENU:\n{menu_text}\n\n"
        "🎯 Yêu cầu trả lời:\n"
        "• Thân thiện, ngắn gọn.\n"
        "• Dùng emoji phù hợp.\n"
        "• Định dạng mỗi món như: <b>Tên món</b> — vị, nhiệt độ, giá.\n"
        "• Kết thúc bằng câu hỏi mở như: 'Bạn muốn mình gợi ý thêm món khác không? 😊'"
    )

    # Payload gửi đến Gemini
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": system_prompt + "\n\nKhách: " + user_message}]
            }
        ]
    }

    # 🛰️ Gửi yêu cầu tới Gemini API
    response = requests.post(url, json=payload)
    print("🔍 Status:", response.status_code)

    ai_reply = "Xin lỗi, hiện mình chưa thể phản hồi được 😢"

    if response.status_code == 200:
        data = response.json()
        try:
            ai_reply = data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            ai_reply = "Xin lỗi, mình chưa hiểu rõ yêu cầu của bạn 😅."

    # ✨ Format cho đẹp
    ai_reply = (
        ai_reply.replace("**", "<b>")
        .replace("*", "•")
        .replace("\n", "<br>")
    )

    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)
