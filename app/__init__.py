from flask import Flask

app = Flask(__name__)

# Ensure routes are imported after the app is created
from app import routes
