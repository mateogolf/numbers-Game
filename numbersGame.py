from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "countThis"

@app.route('/')
def index():
    if 'someKey' not in session:
        session['someKey'] = random.randrange(0, 101)
    print session['someKey']
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    if session['guess'] < session['someKey']:
        session['hint'] = "Too Low!!"
        return render_template('guess.html')
    elif session['guess'] > session['someKey']:
        session['hint'] = "Too High!!"
        return render_template('guess.html')
    else:
        session['hint'] = "{} was the number!".format(session['guess'])
        return render_template('won.html')
@app.route('/reset')
def reset():
    session['someKey'] = random.randrange(0, 101)
    print session['someKey']
    return redirect('/')

app.run(debug=True)
