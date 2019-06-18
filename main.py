from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def first():
    return render_template('intro_page.html')

@app.route('/register')
def second():
    return render_template('register_form.html')

@app.route('/landing')
def third():
    return render_template('student_landing_page.html')

app.run(debug=True,port=60)

