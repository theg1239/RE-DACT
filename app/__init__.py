from flask import Flask

app = Flask(__name__)

from app import routes  # This should remain at the end to avoid circular imports
