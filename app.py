from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def presentation():
    return render_template('index.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/academic')
def academic():
    return render_template('academic.html')

@app.route('/messagesent')
def confirm():
    return render_template('confirmation.html')