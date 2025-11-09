document.getElementById("askBtn").addEventListener("click", async () => {
    const question = document.getElementById("question").value.trim();
    const answerDiv = document.getElementById("answer");
    answerDiv.textContent = "Loading...";

    let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    const url = new URL(tab.url);
    const videoId = url.searchParams.get("v");

    if (!videoId) {
        answerDiv.textContent = "⚠️ Not a YouTube video page!";
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:5000/ask", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ video_id: videoId, question })
        });

        const data = await response.json();
        answerDiv.textContent = data.answer || data.error || "No response";
    } catch (err) {
        answerDiv.textContent = "❌ Error: " + err.message;
    }
});
