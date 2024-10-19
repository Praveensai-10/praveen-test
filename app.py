from flask import Flask, render_template
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(_name_)

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

    # Render the index.html template with data
    return render_template('index.html', name=full_name, username=system_username, server_time=server_time, top_output=top_output)

if _name_ == '_main_':
    app.run(host='0.0.0.0')