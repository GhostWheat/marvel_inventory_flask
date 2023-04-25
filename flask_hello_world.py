from flask import Flask #remember, capital letters used for a Class!
app = Flask(__name__) # so we set app = an instance of a flask Class, passing in


@app.route("/") #homepage of website
def hello():
    return "<h1>Hello World in Flask!</h1>"