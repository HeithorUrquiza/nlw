from flask import Flask
from src.main.routes.trips_routes import trips_routes_bp

# Creating a server with Flask
app = Flask(__name__)

# Registering routes in the server
app.register_blueprint(trips_routes_bp)