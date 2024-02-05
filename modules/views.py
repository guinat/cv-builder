from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .extensions import mysql, bcrypt
from modules.alerts import success, danger, info

app_views = Blueprint('app_views', __name__)


@app_views.route('/')
def home():
    return render_template('home.html')


@app_views.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        plain_password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(
            plain_password).decode('utf-8')

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", [email])
        user = cur.fetchone()

        if user:
            danger('Email déjà utilisé')
            return redirect(url_for('app_views.register'))

        cur.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                    (name, email, hashed_password))
        mysql.connection.commit()

        cur.execute("SELECT id FROM users WHERE email = %s", [email])
        new_user = cur.fetchone()
        session['user_id'] = new_user['id']

        cur.close()

        success('Inscription réussie. Vous êtes maintenant connecté.')
        return redirect(url_for('app_views.home'))

    return render_template('register.html')


@app_views.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        plain_password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE email = %s", [email])
        user = cur.fetchone()
        cur.close()

        if user:
            if bcrypt.check_password_hash(user['password'], plain_password):
                session['user_id'] = user['id']
                success('Connexion réussie')
                return redirect(url_for('app_views.home'))
            else:
                danger('Mot de passe incorrect')
        else:
            info('Email non trouvé. Veuillez vous inscrire.')
            return redirect(url_for('app_views.register'))

    return render_template('login.html')


@app_views.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('Vous êtes déconnecté.', 'info')
    return redirect(url_for('app_views.home'))
