import json
from time import time
from random import random
from flask import Flask, render_template, flash, request, make_response
from wtforms import Form, StringField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    name = StringField('name:', validators=[validators.required()])
    azure_id = StringField('azure_id', validators=[validators.required(), validators.Length(min=6, max=35)])
    connection_string = StringField('connection_string',
                                    validators=[validators.required(), validators.Length(min=3, max=35)])


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)

    print(form.errors)
    if request.method == 'POST':
        name = request.form['name']
        azure_id = request.form['azure_id']
        connection_string = request.form['connection_string']
        print(name, " ", azure_id, " ", connection_string)

        if form.validate():
            # Save the comment here.
            flash('Thanks for the registration of ' + name)
            # We now write the data to the Data container
            import zerorpc

            c = zerorpc.Client()
            c.connect("tcp://data:4242")
            print(c.write_to_yaml(azure_id, connection_string))
        else:
            print(form.errors)
            flash('Error: All the form fields are required. ')

    return render_template('hello.html', form=form)


@app.route("/stats")
def stats():
    return render_template('stats.html', data='test')


@app.route('/live-data')
def live_data():
    # Create a PHP array and echo it as JSON
    data = [time() * 1000, random() * 100]
    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
