from flask import request
from newcomer import app, db
from newcomer.models import Feedback

@app.route('/feedback', methods=['POST'])
def receive_feedback():
    #if args is null or empty get request.form['content'] else args
    content =request.form['content']
    return content
    
    
    
@app.route('/about', methods=['GET'])
def about():
    return 'This is the about page'

