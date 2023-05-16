# whereas .env is used for app configuration, we should use .flaskenv for Flask CLI config commands.
# the example given was:
SECRET_KEY='tempsecretkey'
FLASK_APP=flask_tutorial/flask_hello_world.py
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_RUN_PORT = 5003


# other CLI options for the .flaskenv:

# FLASK_APP is the main flask python file to run
# FLASK_ENV controls the environment
# FLASK_DEBUG enables debug mode
# FLASK_RUN_EXTRA_FILES is a list of files 'that will be watched by the reloader in addition to the Python modules'
# FLASK_RUN_HOST is the host you want to bind your app to
# FLASK_RUN_PORT is the port you want to use
# FLASK_RUN_CERT is a certificate file so your app can be run with HTTPS
# FLASK_RUN_KEY is the key file for your CERT

# By default, FLASK_ENV=production. we could 'instantiate a Sentry library' for production but we wouldn't need to for development.