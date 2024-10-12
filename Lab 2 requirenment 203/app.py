from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/football_quiz', methods=['POST'])
def football_quiz():
    email = request.form.get('email')
    password = request.form.get('password')
    
    return render_template('football_quiz.html')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():

    q1 = request.form.get('q1')
    q2 = request.form.get('q2').strip()
    q3 = request.form.get('q3')
    q4 = request.form.get('q4').strip()

    correct_answers = {
        'q1': 'Argentina', 
        'q2': '8',       
        'q3': 'England', 
        'q4': '900'      
    }

    score = 0
    if q1 == correct_answers['q1']:
        score += 1
    if q2 == correct_answers['q2']:
        score += 1
    if q3 == correct_answers['q3']:
        score += 1
    if q4 == correct_answers['q4']:
        score += 1

    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)