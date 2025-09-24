const backendUrl = "https://YOUR_BACKEND_URL"; // Ganti dengan URL Railway backend Anda

function sendMessage() {
    const msg = document.getElementById("messageInput").value;
    fetch(`${backendUrl}/send`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
    })
    .then(res => res.json())
    .then(data => {
        alert("Pesan terkirim: " + data.message);
        document.getElementById("messageInput").value = "";
    });
}

function fetchMessages() {
    fetch(`${backendUrl.replace('producer', 'consumer')}/receive`)
        .then(res => res.json())
        .then(data => {
            const ul = document.getElementById("messages");
            ul.innerHTML = "";
            data.messages.forEach(msg => {
                const li = document.createElement("li");
                li.textContent = msg;
                ul.appendChild(li);
            });
        });
}

setInterval(fetchMessages, 2000); // Refresh pesan tiap 2 detik
