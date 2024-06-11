import os.path
import sqlite3
from flask import Flask, render_template, url_for, g, request, flash, redirect

from dbpri import FDataBase
from admin.admin import admin

DATABASE = 'comands.db'
DEBUG = True
SECRET_KEY = 'krieuiugeuowangoim'
app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'comands.db')))
app.register_blueprint(admin, url_prefix='/admin')


def connect_db():
    coon = sqlite3.connect(app.config['DATABASE'])
    coon.row_factory = sqlite3.Row
    return coon


def create_db():
    db = connect_db()
    with app.open_resource('sql.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


def get_db():
    ''' Соединение с БД '''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db
    pass

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/admin_index')
def admin_index():
    return  render_template("admin_index.html")


@app.route('/comands', methods=["POST", "GET"])
def addCommand():
    db = get_db()
    dbase = FDataBase(db)
    if request.method == 'POST':
        if len(request.form['name_of_comand']) > 1 and len(request.form['achivements']) > 2 and len(request.form['sostav']) > 2 and len(request.form['identif']) > 2:
            res = dbase.addCommand(request.form['name_of_comand'], request.form['achivements'], request.form['sostav'], request.form['identif'])
            if not res:
                flash('Ошибка добавления', category='error')
            else:
                flash('', category='success')
        else:
            flash('Ошибка добавления', category='error')
    return render_template('comands.html', menu=dbase.getMenu())


@app.route('/Show_Commands', methods=["GET"])
def showComands():
    db = get_db()
    dbase = FDataBase(db)
    res = dbase.getCommand()
    return render_template('Show_Commands.html', res=res)


@app.route('/Show_Commands/del/<int:id>')
def delComands(id):
    db = get_db()
    dbase = FDataBase(db)
    delete = dbase.delCommand(id)
    res = dbase.getCommand()
    return redirect(url_for('showComands'))






if __name__ == "__main__":
    # db = connect_db()
    create_db()
    app.run(debug=True)
