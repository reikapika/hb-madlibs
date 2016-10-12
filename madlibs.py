from random import choice, randint, sample

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """User chooses to play game."""

    response = request.args.get("game")

    if response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """The madlib game."""

    friends = request.args.get("madlib-friends")
    color = request.args.get("madlib-color")
    noun = request.args.get("madlib-noun")
    adjective = request.args.get("madlib-adjective")
    celebrity = request.args.get("madlib-celebrity")
    verb = request.args.getlist("madlib-verb")
    city = request.args.get("madlib-city")
    decision = randint(1, 3)

    return render_template("madlib.html", friends=friends, color=color, 
                            noun=noun, adjective=adjective, celebrity=celebrity,
                            verb=verb, city=city, decision=decision)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
