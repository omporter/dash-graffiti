from flask import Flask, render_template, flash, request
from lib.graffiti import generate_graffiti_address
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27fdlk43jvn4d441f2b6176a'


class ReusableForm(Form):
    string = TextField(
        'Graffiti (max 20 chars):', validators=[validators.required()])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        string = request.form['string']
        if form.validate():
            # Save the comment here.
            flash('Write graffiti "' + string +
                  '" to blockchain by sending some duffs to:')
            flash('')
            flash(generate_graffiti_address(string))
        else:
            flash('All the form fields are required. ')

    return render_template('index.html', form=form)

if __name__ == "__main__":
    app.run()
