import sqlalchemy
from flask import Blueprint, render_template, url_for, redirect
from app.models import StackCount, db

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():

    stack = StackCount.query.order_by(sqlalchemy.desc(StackCount.id)).first()
    
    return render_template('index.html', stack_count=stack.count)

@main_bp.route('/increment')
def increment_stack():
    try:
        stack = StackCount.query.order_by(sqlalchemy.desc(StackCount.id)).first()
        stack.count = stack.count + 1
        db.session.commit()
    except Exception as e:
        print('Unable to increase stack count')
        return 'Internal Serval Error', 500

    return redirect(url_for('main_bp.index'))
