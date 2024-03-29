
# The script above simply creates the application object as an instance of class Flask imported from the flask package.
# The __name__ variable passed to the Flask class is a Python predefined variable,
# which is set to the name of the module in which it is used. Flask uses the location of the module
# passed here as a starting point when it needs to load associated resources such as template files

# For all practical purposes, passing __name__ is almost always going to configure Flask in the correct way.
# The application then imports the routes module, which doesn't exist yet.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
#  The app package is defined by the app directory and the __init__.py script,
# and is referenced in the from app import routes statement. The app variable is defined
# as an instance of class Flask in the __init__.py script, which makes it a member of the app package.

# The routes module is imported at the bottom and not at the top of the script as normally done.
# This is done as a workaround to circular imports, a common problem with Flask applications.
# The routes module needs to import the app variable defined in this script, so putting one of the
# reciprocal imports at the bottom avoids the error that results from the mutual references between these two files.