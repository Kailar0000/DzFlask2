from flask import Flask, render_template, request, redirect
from data_base import db, User
from form import LoginFrom
from hashlib import sha256

app = Flask(__name__)

@app.cli.command("init-db")
def init_db():
    db.create_all()

@app.route("/")
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        new_user = User(name=form.username.data,
                        email=form.email.data,
                        paswword=sha256(form.password.data.encond(enconding="UTF-8")).hexdigest())
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
