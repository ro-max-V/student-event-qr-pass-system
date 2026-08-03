# Student Event Registration & QR Pass Management System

A Flask-based application that allows students to register for events and receive a QR-based event pass.

## Features

- Student Registration Form
- QR Pass Generation
- SQLite Database Storage
- Automatic QR Image Creation
- QR Pass Display After Registration

## Tech Stack

- Python
- Flask
- SQLite
- HTML
- CSS

## Project Structure

QR_EVENT/
├── app.py
├── requirements.txt
├── static/
│   └── qrcodes/
├── templates/
│   └── index.html

## Future Improvements

- Admin Dashboard
- Duplicate Registration Detection
- QR Verification
- Attendance Tracking
- AWS Migration

## Screenshot

![Application Screenshot](screenshots/home.png)
![QR generation Screenshot](screenshots/qr_generated.jpeg)

## How to Run

1. Clone the repository

```bash
git clone <repo-url>
pip install -r requirements.txt
python app.py
