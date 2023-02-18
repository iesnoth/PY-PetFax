from petfax import create_app
app = create_app()
#Note: Creating a global app instance with the application factory is
#different from creating it directly with Flask.
# Here, we're creating the app instance with all our custom logic already loaded into it.

