import subprocess
import time
from flask import Flask
from threading import Thread

# --- SERVER KO ZINDA RAKHNE WALA CODE ---
app = Flask('')

@app.route('/')
def home():
    return "Server Running! Bot 1 & Bot 2 Active."

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# --- BOTS START KARNE WALA CODE ---
if __name__ == "__main__":
    keep_alive()  # Server start
    print("✅ Server Started on Port 8080")

    # Bot 1
    print("🚀 Starting Bot 1...")
    p1 = subprocess.Popen(["python", "main.py"])

    time.sleep(10) # 10 second ka gap

    # Bot 2
    print("🚀 Starting Bot 2...")
    p2 = subprocess.Popen(["python", "main2.py"])

    p1.wait()
    p2.wait()
