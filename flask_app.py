
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request # the numbers from our form code, to be available to our Flask code need to be done via the form attribute of a global variable called request
from processing import do_calculation

app = Flask(__name__) # This creates a Flask application to run the code
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"]) # by defult Flask functions only accept get methods, so need to stipulate POST method also
# The @app.route("/") decorator specifies that the following function is what happens when a user goes to the location "/". For another page you would specify '/foo' instead
def adder_page():
    # This code is validating the errors if a user does not type a number, this code runs if the METHOD is POST
    errors = ""
    if request.method == "POST":
        number1 = None
        number2 = None
        try:
            number1 = float(request.form["number1"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number1"])  #What is the {!r} and where does it get its value from
        try:
            number2 = float(request.form["number2"])
        except:
            errors += "<p>{!r} is not a number.</p>\n".format(request.form["number2"])

        if number1 is not None and number2 is not None:
            result = do_calculation(number1, number2)
            return '''
                <html>
                    <body>
                        <p>The result is {result}</p>
                        <p><a href="/">Click here to calculate again</a>
                    </body>
                </html>
            '''.format(result=result)

    return '''
        <html>
            <body>
                {errors}
                <p>Enter your numbers:</p>
                <form method="post" action="."> <! -- this states that there is an 'action' on the website, when 'submit' is clicked it should request the same page with 'post' method -->
                    <p><input name="number1" /></p>
                    <p><input name="number2" /></p>
                    <p><input type="submit" value="Do calculation" /></p>
                </form>
            </body>
        </html>
    '''.format(errors=errors)


