from flask import Flask

def create_app():
    app = Flask(__name__)

    # Blueprint 등록
    from app.routes import preprocess_blueprint
    app.register_blueprint(preprocess_blueprint)

    return app
