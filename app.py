# Importing Packages
from flask import Flask, render_template, request
from wtforms import Form, validators, StringField
from rand import techno

# Flask Constructor
app = Flask(__name__)

# Using StringField to take the input in form of a String
class InputForm(Form):
    r = StringField(validators=[validators.InputRequired()])

# Calling the decorator to tell the application which URL should call the index() funtion
@app.route('/', methods=['GET', 'POST'])
# Declaring the function to take the data from the input field and calls the techno() funtion to return the output
def index():
    # Sending data from HTML form to the Python Script
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        # Storing the form input field data
        r = form.r.data
        # Calling the techno() function and storing its result
        s = techno(r)
    else:
        s = None

    # Returning the techno() function data on the page indexi.html
    return render_template("indexi.html", form=form, s=s)


# Calling out the entry point
if __name__ == '__main__':
    app.run(debug=True)
