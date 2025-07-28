from flask import Flask, request
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = "8136665096:AAE7tZEon4MrDhYy4OBPgEQ9Q4vip04wjH4"  # Замените на реальный токен
TELEGRAM_CHAT_ID = "6109281862"    # Замените на ID чата/группы

@app.route('/webhook', methods=['POST'])
def webhook():
    alert = request.get_json()
    message = alert.get('text', '🚨 Новый алерт!')
    
    # Отправка в Telegram
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    })
    return "OK", 200

if __name__ == '__main__':
    app.run()