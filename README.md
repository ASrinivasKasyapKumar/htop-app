# Flask Htop App

This project is a simple Flask application that provides an `/htop` endpoint. The endpoint displays system information including the user's full name, system username, server time in IST, and the output of the `top` command.

## Project Structure

```
flask-htop-app
├── app.py                # Main application file
├── templates
│   └── htop.html        # HTML template for the /htop endpoint
├── static
│   └── css
│       └── style.css    # CSS styles for the htop.html template
├── requirements.txt      # List of dependencies
└── README.md             # Project documentation
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/your-username/flask-htop-app.git
   cd flask-htop-app
   ```

2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```
   python app.py
   ```

4. **Access the application:**
   Open your web browser and navigate to `http://localhost:5000/htop` to view the information.

## Usage

The `/htop` endpoint will display:
- Your full name
- System username
- Server time in IST
- Output of the `top` command

Make sure to keep the Codespace running to maintain access to the endpoint.