import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Flask app configuration")

    # Flask 설정
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host address")
    parser.add_argument("--port", type=int, default=10103, help="Port number")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    
    
    return parser.parse_args()

# Global config 객체 생성
args = parse_args()
