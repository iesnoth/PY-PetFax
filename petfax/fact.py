from flask import (Blueprint,render_template,request,redirect)

bp = Blueprint('fact', __name__, url_prefix="/facts")

#add a new fact
#type POST
@bp.route('/new')
def add_fact():
    return render_template('facts/new.html')


@bp.route('/', methods=['GET','POST'])
def index():
    if request.form == 'POST':
        print(request.form)
        return redirect('/facts')

    return render_template('facts/index.html')
