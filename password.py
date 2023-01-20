from flask import Flask, render_template, request
import random

app = Flask(__name__)

#creation of functions which will be mapped to the URL
#function to render the template file, called index.html, needed to create the webpage features where the password generator will work
@app.route('/')
def index():
    return render_template('index.html')

#function to describe, create and show the password
@app.route('/pass/', methods=['GET'])
def show_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    signs = ['!', '#', '@', '&', '%']

    random_letters = random.sample(letters, 7)
    random_upper_letters = random.sample(letters, 3)
    random_upper_letters = [x.upper() for x in random_upper_letters]
    random_numbers = random.sample(numbers, 2)
    random_signs = random.sample(signs, 2)
    p = random_letters + random_upper_letters + random_numbers + random_signs

    random.shuffle(p)

    password = ''
    password = password.join(p)

    show_password = password

    return render_template('index.html', show_password = show_password)

#conditional statement that will enable the website to run as far as the conditions are valid
if __name__ == "__main__":
    app.run(debug=True)
