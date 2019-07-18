# The routes are the different URLs that the application implements.
# In Flask, handlers for the application routes are written as Python functions, called view functions.
# View functions are mapped to one or more route URLs so that Flask knows what logic to
# execute when a client requests a given URL

from flask import render_template

from app import app

# decorators, a unique feature of the Python language
# A decorator modifies the function that follows it
# A common pattern with decorators is to use them to register functions as callbacks for certain events
# In this case, the @app.route decorator creates an association between the URL given as an argument and the function.
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'ron'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

# render_template() takes a template filename and a variable list of template arguments
# and returns the same template, but with all the placeholders in it replaced with actual values
# render_template() function invokes the Jinja2 template engine that comes bundled with the Flask framework.
# Jinja2 substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the
# render_template() call.