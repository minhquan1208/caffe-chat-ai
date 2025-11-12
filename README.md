<h1 align="center">☕ AI COFFEE RECOMMENDER</h1>
<p align="center">
<img width="236" height="214" alt="image" src="![Uploading image.png…]()
" />
</p>]

<h2 align="center">Trợ lý AI gợi ý đồ uống cà phê thông minh</h2>

<p align="left">
  <b>AI Coffee Recommender</b> là ứng dụng web sử dụng công nghệ trí tuệ nhân tạo để gợi ý loại cà phê phù hợp với sở thích người dùng.
  Người dùng có thể nhập yêu cầu như “Tôi thích đồ uống lạnh, ít ngọt” — hệ thống sẽ tự động phân tích và đề xuất món cà phê phù hợp dựa trên dữ liệu menu.
</p>

---

<h1>🌟 GIỚI THIỆU</h1>

📌 Gợi ý món cà phê thông minh dựa trên khẩu vị người dùng.<br>
💬 Tương tác trực quan qua giao diện web.<br>
🧠 Tích hợp OpenAI API để hiểu và phản hồi ngữ cảnh bằng tiếng Việt.<br>
🚀 Dễ dàng triển khai trên môi trường cục bộ hoặc cloud.<br>

---

<h1>🏗️ CẤU TRÚC DỰ ÁN</h1>

<div>

<pre>

📦 coffee-ai-recommender
│
├── 📂 data
│   └── menu.json               # Danh sách các loại đồ uống (tên, vị, nhiệt độ,...)
│
├── 📂 static
│   ├── script.js               # Gửi yêu cầu từ người dùng đến server Flask
│   └── style.css               # Giao diện trang web
│
├── 📂 templates
│   └── index.html              # Giao diện chính của ứng dụng
│
├── .env                        # Chứa API key của OpenAI (không public)
└── app.py                      # File chạy chính (Flask server)


</pre>

</div>





---

<h1>🛠️ CÔNG NGHỆ SỬ DỤNG</h1>

<div>

🐍 **Ngôn ngữ:** Python 3.x<br>
🌐 **Framework:** Flask<br>
🧠 **AI Engine:** OpenAI GPT API<br>
🎨 **Frontend:** HTML, CSS, JavaScript (Fetch API)<br>

</div>

---

<h1>🧩 YÊU CẦU HỆ THỐNG</h1>

💻 **Phần mềm:**
- Python >= 3.9  
- Flask  
- OpenAI Python SDK  

📦 **Cài đặt thư viện cần thiết:**
```bash
pip install flask openai python-dotenv

