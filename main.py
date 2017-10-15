from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="POST"> 
            <label for="first-name">First Name: </label>
            <input id="first-name" type="text" name="first_name"/>
            <input type="submit"/>
        </form>
    </body>
</html>
"""


@app.route("/") #needs source activate to run -- receives request
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    ##first_name = request.args.get('first_name') #get, not post
    first_name = request.form['first_name']
    return '<h1>Hello, ' + first_name + '!<h/1>'

app.run()