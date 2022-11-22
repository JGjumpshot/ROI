import waitress
from app import app
if __name__ == '__main__':
    waitress.serve(app, port=8080, url_scheme="https")
