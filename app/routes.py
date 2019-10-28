from app import app
from flask import render_template,flash,request
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@app.route('/upload', methods=['GET','POST'])

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


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
