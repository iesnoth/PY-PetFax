from flask import Flask

def create_app():
    app = Flask (__name__)

    #index route
    #type GET
    @app.route('/')
    def hello():
        return 'Hello, this is PetFax!'

    return app