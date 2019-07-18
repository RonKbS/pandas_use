# This is a Python script at the top-level that defines the Flask application instance.

# bashrc => bash run commands

from app import app
# To handle the web forms in this application, use is made of the Flask-WTF extension,
# which is a thin wrapper around the WTForms package that nicely integrates it with Flask.
# Extensions are a very important part of the Flask ecosystem, as they provide solutions
# to problems that Flask is intentionally not opinionated about.

# The Flask-WTF extension uses Python classes to represent web forms. A form class simply defines the
# fields of the form as class variables.