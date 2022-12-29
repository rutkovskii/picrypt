from app import create_app
from api import api_blueprint

app = create_app()
app.register_blueprint(api_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)

