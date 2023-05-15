from flask import Flask
from flask_migrate import Migrate
from routes.blueprint import blueprint
from models.models import db
from security import login_manager


def create_app():
    app = Flask(__name__)  # flask app object
    app.config.from_object('config')  # Configuring from Python Files

    db.init_app(app)  # Initializing the database
    return app


app = create_app()  # Creating the app
# Registering the blueprint
app.register_blueprint(blueprint, url_prefix='/v1/shop')
migrate = Migrate(app, db)  # Initializing the migration

# Config flask login
login_manager.init_app(app)


if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)

