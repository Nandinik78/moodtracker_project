from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('moodtracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS moods (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    date TEXT,
                    mood TEXT,
                    note TEXT
                )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def index():
    conn = sqlite3.connect('moodtracker.db')
    c = conn.cursor()
    c.execute('SELECT * FROM moods ORDER BY date DESC')
    entries = c.fetchall()
    conn.close()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add():
    mood = request.form['mood']
    note = request.form['note']
    date = datetime.now().strftime('%Y-%m-%d')
    conn = sqlite3.connect('moodtracker.db')
    c = conn.cursor()
    c.execute("INSERT INTO moods (date, mood, note) VALUES (?, ?, ?)", (date, mood, note))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/chart')
def chart():
    conn = sqlite3.connect('moodtracker.db')
    c = conn.cursor()
    c.execute("SELECT date, mood FROM moods")
    data = c.fetchall()
    conn.close()
    return render_template('chart.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
