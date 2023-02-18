from flask import Flask

def create_app():
    app = Flask (__name__)

    #index route
    #type GET
    @app.route('/')
    def hello():
        return 'Hello, this is PetFax!'

    #register the Blueprints
    from . import pet
    app.register_blueprint(pet.bp)
    
    from . import fact
    app.register_blueprint(fact.bp)


    # @app.route('/pets/<int:pet_id>')
    # def one_pet(pet_id):
    #     return f'Post {pet_id}'

    return app