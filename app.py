from flask import Flask
from flask import render_template, redirect, request, url_for, flash
from flask.ext.login import login_user, logout_user, login_required, current_user
from forms import Login, Prof_signup
from flask_bootstrap import Bootstrap

from models import User

bootstrap = Bootstrap()

app = Flask(__name__)

@app.route('/', methods =['GET','POST'])
def signup():
    form = signup
    return render_template('index.html', form=form)


@app.route('/hello', methods=['GET', 'POST'])
def helloworld():
    return render_template('hello.html')



if __name__ == '__main__':
    app.run()
