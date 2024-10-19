from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Name and Username
    full_name = "P.Praveen Sai" 
    system_username = os.getenv("USER") or os.getenv("USERNAME")

    # Server Time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Top command output
    top_output = subprocess.getoutput('top -bn1 | head -10')


    return f"""
    <html>
    <body>
        <p><b>Name:</b> {full_name}</p>
        <p><b>Username:</b> {system_username}</p>
        <p><b>Server Time (IST):</b> {server_time}</p>
        <h2>Top Command Output:</h2>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=5000, debug=True)