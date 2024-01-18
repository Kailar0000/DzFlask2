from flask import Flask, render_template, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from hashlib import sha256

from data_base import db, User
from form import LoginFrom

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()

@app.route("/")
def login():
    form = LoginFrom()
    if form.validate_on_submit():
        new_user = User(first_name=form.first_name.data,
                        second_name=form.second_name.data,
                        email=form.email.data,
                        paswword=sha256(form.password.data.encond(enconding="UTF-8")).hexdigest())
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
