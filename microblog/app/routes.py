# The routes are the different URLs that the application implements.
# In Flask, handlers for the application routes are written as Python functions, called view functions.
# View functions are mapped to one or more route URLs so that Flask knows what logic to
# execute when a client requests a given URL

from app import app

# decorators, a unique feature of the Python language
# A decorator modifies the function that follows it
# A common pattern with decorators is to use them to register functions as callbacks for certain events
# In this case, the @app.route decorator creates an association between the URL given as an argument and the function.
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
