from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask, redirect, render_template

app = Flask(__name__)

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('example.html', title='Авторизация', form=form)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
