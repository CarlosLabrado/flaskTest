from gevent import monkey

monkey.patch_all()
import json
from flask import Flask, render_template, flash, request, make_response
from wtforms import Form, StringField, validators, StringField, SubmitField
from zerorpc_client import ZeroClient

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

            client = ZeroClient().get_instance().get_client()

            print(client.write_to_yaml(azure_id, connection_string))
        else:
            print(form.errors)
            flash('Error: All the form fields are required. ')

    return render_template('hello.html', form=form)


@app.route("/stats", methods=['GET', 'POST'])
def stats():
    client = ZeroClient().get_instance().get_client()

    status = client.get_status()
    settings = client.get_settings()

    return render_template('stats.html', data='test', status=status, settings=settings)


@app.route('/live-data')
def live_data():
    # Create a PHP array and echo it as JSON
    client = ZeroClient().get_instance().get_client()

    data = client.get_dyna_point()

    response = make_response(json.dumps(data))
    response.content_type = 'application/json'
    return response


@app.route('/refreshStatus', methods=['POST'])
def refresh_status():
    client = ZeroClient().get_instance().get_client()
    status = client.get_status()

    return json.dumps(status)


@app.route('/updateSettings', methods=['POST'])
def update_settings():
    json_settings = None
    if request.method == "POST":
        settings = json.dumps(request.values.dicts[1])
        json_settings = json.loads(settings)

        print(json_settings)

    client = ZeroClient().get_instance().get_client()
    client.update_settings(json_settings)

    return ""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
