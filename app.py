from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import (
    UserMixin,
    login_user,
    LoginManager,
    current_user,
    logout_user,
    login_required,
)

# Initialize the login manager
login_manager = LoginManager()

# Set the session protection level
login_manager.session_protection = "strong"

# Set the login view for unauthorized users
login_manager.login_view = "login"

# Set the message category for flashed messages
login_manager.login_message_category = "info"

# Initialize the SQLAlchemy database
db = SQLAlchemy()

# Initialize the database migration tool
migrate = Migrate()

# Initialize the Bcrypt password hashing tool
bcrypt = Bcrypt()


def create_app():
    # Create a Flask application instance
    app = Flask(__name__)

    # Set the secret key for the app
    app.secret_key = "secret-key"

    # Set the URI for the SQLite database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

    # Set to True to enable tracking modifications in SQLAlchemy
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    # Initialize the login manager with the Flask app instance
    login_manager.init_app(app)

    # Initialize the SQLAlchemy database with the Flask app instance
    db.init_app(app)

    # Initialize the migration tool with the Flask app instance & SQLAlchemy database instance
    migrate.init_app(app, db)

    # Initialize the Bcrypt password hashing tool with the Flask app instance
    bcrypt.init_app(app)

    # Return the Flask app instance
    return app
