from app import create_app
from config import args

app = create_app()

if __name__ == "__main__":
    app.run(host=args.host, port=args.port, debug=args.debug)