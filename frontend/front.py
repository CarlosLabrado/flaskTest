from flask import Flask, render_template, flash, request
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
            flash('Thanks for registration ' + name)
            import zerorpc

            c = zerorpc.Client()
            c.connect("tcp://127.0.0.1:4242")
            print(c.add_man("carlos"))
        else:
            print(form.errors)
            flash('Error: All the form fields are required. ')

    return render_template('hello.html', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
