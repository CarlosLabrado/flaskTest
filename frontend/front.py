from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
