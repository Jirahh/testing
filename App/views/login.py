from flask import Blueprint, redirect, render_template, request, send_from_directory
from flask_jwt import jwt_required
from flask_login import LoginManager, current_user, login_user, login_required

from App.controllers import (
    get_user_by_username
)

login_views = Blueprint('login_views', __name__, template_folder='../templates')

@login_views.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')

@login_views.route('/login', methods=['POST'])
def loginAction():
    data = request.form
    user = user.query.filter_by(username = data['username']).first()
    if user and user.check_password(data['password']):
        flash('Logged in successfully.')
        login_user(user)
        return redirect('/index')
    else:
        flash('Invalid username or password.')
    return redirect('/')