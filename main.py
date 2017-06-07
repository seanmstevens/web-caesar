from flask import Flask, request
from caesar import rotate_string
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    template = jinja_env.get_template('caesar_form.html')
    return template.render(title = "Web Caesar")

def is_integer(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

@app.route('/', methods = ['POST'])
def encrypt():
    rotation = request.form['rot']
    text = request.form['text']

    rotation = int(rotation)
    encrypted_message = rotate_string(text, rotation)
    template = jinja_env.get_template('caesar_form.html')
    return template.render(message = encrypted_message, title = "Web Caesar")

app.run()