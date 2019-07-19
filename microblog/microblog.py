# This is a Python script at the top-level that defines the Flask application instance.

# bashrc => bash run commands

from app import app, db
from app.models import User, Post

# flask shell has a nifty trick of you being able to configure a "shell context",
# which is a list of other symbols to pre-import.

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
