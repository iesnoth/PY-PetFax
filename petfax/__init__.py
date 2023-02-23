from flask import Flask
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #db stuff
    from . import models
    models.db.init_app(app)

    migrate = Migrate(app, models.db)

    # index route
    # type GET
    @app.route('/')
    def hello():
        return 'Hello, this is PetFax!'

    # register the Blueprints
    from . import pet
    app.register_blueprint(pet.bp)

    from . import fact
    app.register_blueprint(fact.bp)

    # @app.route('/pets/<int:pet_id>')
    # def one_pet(pet_id):
    #     return f'Post {pet_id}'

    return app
