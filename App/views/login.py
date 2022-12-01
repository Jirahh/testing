from flask import Blueprint, redirect, render_template, request, send_from_directory

login_views = Blueprint('login_views', __name__, template_folder='../templates')

@login_views.route('/', methods=['GET'])
def login_page():
    return render_template('login.html')