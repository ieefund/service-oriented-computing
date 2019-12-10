import pytz
import sqlalchemy
from sqlalchemy import create_engine, and_, or_, Unicode, DateTime, Boolean
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

print(sqlalchemy.__version__)

engine = create_engine(
    'sqlite:///database/comments.db',
    echo=False,
    connect_args={'check_same_thread': False})
Base = declarative_base()

class comment(db.Model):
    comment = db.Column(db.String(50))

def __init__(self, comment):
    self.comment = comment

db.create_all()

@app.route('/img', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['comment']:
            flash("Please enter all the fields", 'error')
        else:
            comment = comment(request.form['comment'])

        db.session.add(comment)
        db.session.commit()

        return redirect(url_for('img'))
    return render_template('img.html')