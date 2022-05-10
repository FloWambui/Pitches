from flask import render_template
from . import main


@main.route('/')
def home():
    title = 'The Pitch Hub'
    data = "Welcome to Pitch Hub"
    
    return render_template('index.html', title=title, datum=data)