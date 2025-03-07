from flask import Flask, Response
import os
import subprocess
import datetime
import pytz
import psutil

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Your Full Name"  # Replace with your actual full name
    username = os.getlogin() if hasattr(os, 'getlogin') else os.environ.get("USER", "unknown")
    ist = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S.%f%z")
    
    # Retrieve system usage data
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    
    # Get top command output
    top_output = subprocess.getoutput("top -b -n 1")

    html = f"""
    <html>
      <head><title>HTop Endpoint</title></head>
      <body>
        <h2>HTop Information</h2>
        <p>Name: {name}</p>
        <p>Username: {username}</p>
        <p>Server Time (IST): {server_time}</p>
        <h3>System Usage:</h3>
        <p>CPU Usage: {cpu_usage}%</p>
        <p>Memory Usage: {memory_usage}%</p>
        <h3>Top Output:</h3>
        <pre>{top_output}</pre>
      </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
