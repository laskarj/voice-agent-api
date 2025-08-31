
---

## 🔹 Backend (FastAPI)

Endpoints:
- `api/v1/webrtc/session` → create WebRTC session (SDP exchange)
- `api/v1/transcribe` → send audio → Whisper → text
- `api/v1/chat` → text → GPT-4o-mini → AI response
- `api/v1/tts` → text → TTS (OpenAI/ElevenLabs) → audio

---

**Pipeline**:  
React (audio) → FastAPI → Whisper (ASR) → GPT-4o-mini → TTS → React (audio out)

---
