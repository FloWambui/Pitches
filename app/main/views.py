from flask import render_template
from . import main


@main.route('/')
def home():
    title = 'The Pitch Hub'
    message = "Make your Best Impression. "
    
    return render_template('index.html',title=title,message=message)