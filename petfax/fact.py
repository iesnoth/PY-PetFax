from flask import (Blueprint,render_template)

bp = Blueprint('fact', __name__, url_prefix="/facts")

#add a new fact
#type POST
@bp.route('/new')
def add_fact():
    return render_template('facts/new.html')