"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']
DISSNESS = [
      'mean', 'not smart'
]


@app.route('/')
def start_here():
    """Home page."""

    return "<!doctype html><html>Hi! This is the home page. <a href='/hello'>Click to Hello Page</a></html>"


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    options = ''

    for compliment in AWESOMENESS:
      compliment_str = "<option value={}>{}</option>".format(compliment, compliment)
      options += compliment_str

    diss_options = ''

    for diss in DISSNESS:
      diss_str = "<option value={}>{}</option>".format(diss, diss)
      diss_options += diss_str

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person"><br>
          Choose your compliment<br>
          <select name="compliment">
            {}
          </select><br>
          <input type="submit" value="Submit">
        </form>
        <form action="/diss">
          What's your name? <input type="text" name="person"><br>
          Choose your diss<br>
          <select name="diss">
            {}
          </select><br>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """.format(options, diss_options)

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """.format(player=player, compliment=compliment)

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")
    diss = request.args.get("diss")

    return """
    <!doctype html>
    <html>
      <head>
        <title>An Insult</title>
      </head>
      <body>
        Hi, {player}! I think you're {insult}!
      </body>
    </html>
    """.format(player=player, insult=diss)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host='0.0.0.0')
