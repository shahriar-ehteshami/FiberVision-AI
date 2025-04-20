# App factory + Blueprint registration

from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import and register Blueprints
    from .routes.auth import auth_bp
    from .routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app
