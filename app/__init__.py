from flask import Flask

app = Flask(__name__)

# Import routes after the app is defined
from app import routes

if __name__ == '__main__':
    # Check if FLASK_ENV is set to development
    import os
    if os.environ.get('FLASK_ENV') == 'development':
        app.run(debug=True)
    else:
        app.run()
