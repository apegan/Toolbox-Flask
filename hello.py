"""
Alisha Pegan Flask Toolbox
Web page that ask for the user to fill a form, checks if data was
provided, and then displays the results.
"""

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

poll_data = [
    {'name': 'What is your name?'},
    {'age': 'What is your age?'},
    {'ninja': 'Who is your favorite ninja?'}
]

filename = 'data.txt'


@app.route('/')
def home():
    return render_template('student.html', data=poll_data)


@app.route('/login')
def poll():
    response = request.args.get('field')

    out = open(filename, 'a')
    out.write(response + '\n')
    out.close()

    return response


# app.run(host='0.0.0.0')     # run on all public IPS
# app.run(debug=True)         # server will reload on code changes


# @app.route('/')
# def hello_world():
#     return render_template('index.html')


# @app.route('/login', methods=['POST', 'GET'])
# def result():
#     if request.method == 'POST':
#         result = request.form
#         return render_template("login.html", result=result)


if __name__ == '__main__':
    app.run(debug=True)
