from app.home import home_routes
from flask import render_template

@home_routes.route('/')
def home_page():
    return render_template('home.html')