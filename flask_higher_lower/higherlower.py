from flask import Flask
import random
app = Flask(__name__)
print(__name__)

random_number = random.randint(0,9)

@app.route("/")
def disgen():
    return "<h1>Guess a number between 0 and 9</h1> \
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route("/check/<int:guess_number>")
def check(guess_number):
    if guess_number == random_number:
        return f"<h1> You guess well, number was {guess_number}</h1> \
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    if guess_number > random_number:
        return f"<h1> Too High {guess_number} </h1>\
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    if guess_number <  random_number:
        return f"<h1> Too Low {guess_number}</h1> \
    <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)