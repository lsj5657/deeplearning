from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprint 등록
    from app.routes import kolors_blueprint
    app.register_blueprint(kolors_blueprint)

    return app
