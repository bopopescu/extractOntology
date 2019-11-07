from app import app,mongo
from flask import render_template,flash,request
from app.forms import InputForm
from app.models import dataProcess
from bson.json_util import dumps
from wtforms import SelectField
import os
import json

@app.route('/')
@app.route('/index')
def login():
    form = InputForm()
    if form.validate_on_submit():
        return render_template('result.html',title='Result',form=form)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/graph',methods=['POST'])
def generate_graph():
    return render_template('graph.html')

@app.route('/', methods=['POST'])
def my_form_post():
    documents = dumps(mongo.db[request.form['articles']].find({}))
    if request.form['choice']=="tree":
        json_url=os.path.join(os.path.realpath(os.path.dirname(__file__)),"static","flare.json")
        jsonData = json.load(open(json_url))
        return render_template("result.html",title="result",form=request.form['articles'], jsonData=jsonData)
    else:
        return render_template('/graph')

def upload_file():
    if request.method=='POST':
        f=request.files['file']
        return 'file uploaded successfully'
    else:
        return render_template('upload.html')
def index():
    user={'username':'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    return render_template('index.html',title='Home',user=user, posts=posts)

