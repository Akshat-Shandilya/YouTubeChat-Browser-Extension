## YouTubeChat Chrome Extension

A lightweight Chrome extension that lets you **ask questions about YouTube videos** directly from your browser popup.  
It uses a local Python backend to fetch video transcripts and generate AI-powered answers.

---

## Features

- Uses Gemini to analyze YouTube video transcripts  
- Ask natural language questions directly from a browser popup  
- Automatically detects the current YouTube video ID  
- Lightweight Flask backend with CORS support  
- Clean UI built with plain HTML, CSS, and JS  
- Runs locally 

---

## Project Structure

```

project/
├── main.py              # LangChain logic
├── server.py            # Flask API wrapper for chain
├── manifest.json
├── popup.html
├── popup.js
└── styles.css
````
---

## Setup Instructions

### 1️. Clone or Download

```bash
git clone https://github.com/Akshat-Shandilya/youtube-qa-extension.git
cd youtube-qa-extension
```

### 2️. Add API Keys to .env file

Create a .env file in your project’s root directory (next to main.py and server.py), and add your Gemini and Hugging Face credentials:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
HF_API_TOKEN=your_huggingface_auth_token_here
```

These keys are required for the Gemini model and Hugging Face embeddings used inside main.py.

How to get them:

#### Gemini API Key (Google AI Studio)

Go to https://aistudio.google.com/app/apikey
Sign in with your Google account
Click “Create API Key” and copy it

#### Hugging Face Token

Go to https://huggingface.co/settings/tokens
Click “New Token” → choose read access
Copy your token and paste it in .env


### 3. Set Up Backend (Flask API)

Make sure you have Python 3.9+ installed. Install the necessary libraries.
```bash
pip install -r requirements.txt
```

Run your backend:
```bash
python server.py
```

If successful, you’ll see:
```
 * Running on http://127.0.0.1:5000
```


### 4. Load the Extension

1. Open your browser ( Eg. Chrome )
2. Visit `chrome://extensions`
3. Toggle **Developer Mode** (top-right)
4. Click **“Load unpacked”**
5. Select the folder `youtube-qa-extension/`

You should see your extension appear in the toolbar.


### 5. Use It!

1. Open any YouTube video
2. Click the **YouTube Q&A Helper** icon
3. Type your question (e.g. *"What is this video about?"*)
4. Get your Gemini-powered response instantly 

---

## Troubleshooting

| Issue                          | Solution                                                                                   |
| ------------------------------ | ------------------------------------------------------------------------------------------ |
| *Failed to fetch*            | Ensure Flask is running on `http://127.0.0.1:5000` and that CORS is enabled                |
| *Not a YouTube video page!* | Make sure the tab URL contains a `v=` parameter (YouTube video ID)                         |
| *CORS or HTTPS issues*      | Use an ngrok tunnel for testing: `ngrok http 5000` and update `popup.js` & `manifest.json` |

---

## Tech Stack

* **Frontend** – HTML, CSS, JavaScript (Chrome Extension)
* **Backend** – Flask + Flask-CORS
* **Models** – all-MiniLM-L6-v2 (for embeddings) and gemini-2.0-flash (for chat)
* **Transcript** – YouTubeTranscriptAPI
* **Vector Search** – FAISS

---

## Author

**Akshat Shandilya**

---

## License

This project is licensed under the **MIT License** — free to use and modify.
