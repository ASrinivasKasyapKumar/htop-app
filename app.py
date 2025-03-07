from flask import Flask, render_template
from flask_cors import CORS
import os
import datetime
import psutil

app = Flask(__name__)
CORS(app)

@app.route('/htop')
def htop():
    # Get the user's full name and system username
    full_name = "Your Full Name"  # Replace with your actual full name
    username = os.getlogin()

    # Get the current server time in IST
    ist_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))

    # Get system information using psutil
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    return render_template('htop.html', full_name=full_name, username=username, ist_time=ist_time, cpu_usage=cpu_usage, memory_usage=memory_usage)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)