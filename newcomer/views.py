from flask import request
from newcomer import app, db
from newcomer.models import Feedback

@app.route('/feedback', methods=['POST'])
def receive_feedback():
    content = request.form['content']
    # Here is where you would process the feedback with your AI/ML model
    # For now, we'll just echo the feedback
    response = content
    feedback = Feedback(content=content, response=response)
    db.session.add(feedback)
    db.session.commit()
    return response