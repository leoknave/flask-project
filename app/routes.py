from flask import Blueprint, render_template
from .models import User

main = Blueprint('main', __name__, template_folder='../templates')  

@main.route('/')
def index():
    users = User.query.all()
    return render_template('users.html', users=users)
