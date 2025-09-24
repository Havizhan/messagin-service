# Messaging Service

## Struktur Folder

backend/
  - producer.py
  - consumer.py
  - requirements.txt
  - Procfile
frontend/
  - index.html
  - style.css
  - script.js

## Cara Menjalankan

1. Masuk ke folder backend, install requirements:
   pip install -r requirements.txt
2. Jalankan producer:
   uvicorn producer:app --reload --port 8000
3. Jalankan consumer (terminal lain):
   uvicorn consumer:app --reload --port 8001
4. Buka frontend/index.html di browser.

## Deploy
- Deploy backend/producer.py dan backend/consumer.py ke Railway (masing-masing project)
- Deploy frontend ke Netlify/Vercel/GitHub Pages
