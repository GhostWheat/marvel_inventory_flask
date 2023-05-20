from flask import Flask, url_for, render_template

app = Flask(__name__, template_folder='./templates')

@app.route('/',methods=['get','post','put','delete'])
def index():
    return render_template('index.html')
