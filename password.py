from flask import render_template
from flask import request
from flask import Blueprint

password = Blueprint('password', __name__)

@password.route("/password/")
def index():
	return "password"
