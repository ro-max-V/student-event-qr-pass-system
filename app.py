import os, sqlite3, qrcode
from flask import Flask, render_template, request

app = Flask(__name__)

# Ensure folder for storing generated QR images exists
os.makedirs("static/qrcodes", exist_ok=True)

# Initialize local SQLite Database
def init_db():
    conn = sqlite3.connect("event_db.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            reg_no TEXT NOT NULL UNIQUE,
            qr_code_url TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    qr_url = None
    if request.method == "POST":
        name = request.form["name"]
        reg_no = request.form["reg_no"]

        # 1. Generate & Save QR Code locally
        qr_img = qrcode.make(f"Verified Registration:\nName: {name}\nReg No: {reg_no}")
        filename = f"{reg_no}.png"
        file_path = os.path.join("static", "qrcodes", filename)
        qr_img.save(file_path)

        # 2. Set web URL path for displaying image on screen
        qr_url = f"/static/qrcodes/{filename}"

        # 3. Save details to local SQLite DB
        conn = sqlite3.connect("event_db.db")
        cursor = conn.cursor()
        cursor.execute(
            "INSERT OR REPLACE INTO passes (name, reg_no, qr_code_url) VALUES (?, ?, ?)",
            (name, reg_no, qr_url)
        )
        conn.commit()
        conn.close()

    return render_template("index.html", qr_url=qr_url)

if __name__ == "__main__":
    app.run(debug=True, port=5000)