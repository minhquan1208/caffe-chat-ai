document.addEventListener("DOMContentLoaded", () => {
  console.log("✅ Script loaded successfully!");

  const chatBox = document.getElementById("chat-box");
  const input = document.getElementById("user-input");
  const sendBtn = document.getElementById("send-btn");

  // 💬 Hàm thêm tin nhắn
  function addMessage(sender, message) {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("message", sender);
    msgDiv.innerHTML = `<strong>${sender === "user" ? "Bạn" : "AI"}:</strong> ${message}`;
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    return msgDiv;
  }

  // ✨ Hàm tạo hiệu ứng "AI đang gõ..."
  function showTyping() {
    const typingDiv = document.createElement("div");
    typingDiv.classList.add("message", "ai", "typing");
    typingDiv.innerHTML = `<strong>AI:</strong> <span class="dots">...</span>`;
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
    return typingDiv;
  }

  // 🚀 Hàm gửi tin nhắn
  async function sendMessage() {
    const userMsg = input.value.trim();
    if (!userMsg) return;

    addMessage("user", userMsg);
    input.value = "";

    // Hiển thị hiệu ứng typing
    const typingDiv = showTyping();

    try {
      const res = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userMsg })
      });

      if (!res.ok) throw new Error("Lỗi khi gửi tin nhắn");

      const data = await res.json();

      // Xóa hiệu ứng typing
      typingDiv.remove();

      // Hiển thị phản hồi thật
      addMessage("ai", data.reply);
    } catch (err) {
      console.error(err);
      typingDiv.remove();
      addMessage("ai", "⚠️ Có lỗi xảy ra khi kết nối với máy chủ.");
    }
  }

  sendBtn.addEventListener("click", sendMessage);
  input.addEventListener("keypress", e => {
    if (e.key === "Enter") sendMessage();
  });
});
