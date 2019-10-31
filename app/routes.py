from app import app
from flask import render_template,flash,request
from app.forms import InputForm
from wtforms import SelectField

@app.route('/result',methods=['POST'])
def result():

    return render_template("result.html",user=user)

@app.route('/')
@app.route('/index')
@app.route('/upload', methods=['GET','POST'])

@app.route('/login')
def login():
    # clinet = MongoClient('mongodb://127.0.0.1:27017/')
    # database_name = 'extractOntology'
    # database = clinet[database_name]
    # collections = database.collection_names(include_system_collections=False)
    # posts = database.posts
    # name_list = [p['name'] for p in posts.find({'type': "server"})]
    form = InputForm()

    # articles = SelectField(
    #     u'Industry Type',
    #     choices = [('Software', 'software'), ('Sales', 'sales')]
    # )
    if form.validate_on_submit():
        return render_template('result.html',title='Result',form=form)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/', methods=['POST'])
def my_form_post():
    documents = app.mongo.db[request.form['articles']].find({})
    for document in documents:
        print(document)
    return render_template("result.html",title="result",form=request.form['articles'])

def upload_file():
    if request.method=='POST':
        f=request.files['file']
        print('I SAVE FILE')
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

