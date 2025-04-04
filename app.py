from flask import Flask
import os
import subprocess
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "Brijesh Singh"
    username = os.getenv("CODESPACE_NAME", "unknown")
    
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    try:
        top_output = subprocess.check_output("top -bn1 | head -20", shell=True, text=True)
    except Exception as e:
        top_output = f"Error running top: {str(e)}"

    return f"""
    <html>
    <body>
        <h2>Name: {full_name}</h2>
        <h3>Username: {username}</h3>
        <h3>IST Time: {current_time}</h3>
        <h3>Top Output:</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
