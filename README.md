# 🧪 Gemini API Lab

A hands-on repository exploring Google's Gemini models, covering text generation, multimodal processing (image/audio/video), streaming responses, structured outputs, and prompt engineering techniques.

---

## 📌 Features

- *Text Generation & Streaming*: Experimenting with basic prompts, system instructions, and real-time token streaming.
- *Multimodal Capabilities*: Processing visual inputs, document analysis, and multimedia queries.
- *Structured Outputs*: Enforcing JSON schemas and deterministic model outputs for downstream tools.
- *Chat & Context Management*: Multi-turn conversational interfaces retaining session history.
- *Parameter Tuning*: Exploring temperature, top-k, and top-p settings across varied tasks.

---

## 📁 Repository Structure

```text
Gemini-API-Lab/
├── notebooks/              # Jupyter notebooks for interactive prototyping
│   ├── 01_getting_started.ipynb
│   ├── 02_multimodal_tasks.ipynb
│   └── 03_chat_and_streaming.ipynb
├── src/                    # Modular Python scripts and utility functions
│   ├── client.py           # Gemini client setup and configuration
│   └── examples.py         # Standalone scripts demonstrating key features
├── .env.example            # Template for environment variables
├── requirements.txt        # Project dependencies
└── README.md
