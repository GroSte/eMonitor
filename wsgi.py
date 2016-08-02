# start with: gunicorn --bind 0.0.0.0:8000 wsgi:app
from emonitor import app

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
