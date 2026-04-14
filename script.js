async function send() {
    let msg = document.getElementById("msg").value;

    if (msg.trim() === "") return;

    let chatBox = document.getElementById("chatBox");

    // Show user message
    chatBox.innerHTML += `<div class="user">You: ${msg}</div>`;

    // API call
    let res = await fetch("https://ai-mental-wellness-fyz0.onrender.com/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({text: msg})
    });

    let data = await res.json();

    // Show AI response
    chatBox.innerHTML += `
    <div class="bot">
        ${data.reply}
    </div>
`;

    // Auto scroll
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear input
    document.getElementById("msg").value = "";
}
