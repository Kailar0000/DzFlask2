from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("start.html")

@app.post('/start/')
def start():
    response = make_response(render_template("start.html"))
    name = request.form.get('name')
    mail = request.form.get('mail')
    response = make_response(redirect(url_for('hello', name=name)))
    response.set_cookie('name', name)
    response.set_cookie('mail', mail)
    return response


@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)


@app.post('/exit/')
def exit():
    response = make_response(redirect(url_for('index')))
    response.set_cookie('name', 'bar', max_age=0)
    response.set_cookie('mail', 'bar', max_age=0)
    return response


if __name__ == "__main__":
    app.run(debug=True)
