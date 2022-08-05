#from crypt import methods
from crypt import methods
from email.policy import default
from flask import Blueprint, request
#from flask import render_template
from flask.views import MethodView
#from requests import request
from .config import SQLManager

bp = Blueprint('blog', __name__, url_prefix='/blog', 
                static_folder='static', template_folder='templates')


class categoryAPI(MethodView):
    def get(self, id=None):
        with SQLManager() as sqlm:
            if not id:
                results = sqlm.get_list('SELECT `id`,`name`,`icon`,`add_date`,`pub_date` \
                                         FROM `Category` \
                                         WHERE 1=1')
                return {
                    'status':'success',
                    'message':'数据查询成功',
                    'result':results
                }
            results = sqlm.get_one('SELECT `id`,`name`,`icon`,`add_date`,`pub_date` \
                                         FROM `Category` \
                                         WHERE `id`=%s', (id,))
            return {
                    'status':'success',
                    'message':'数据查询成功',
                    'result':results
                }


bp.add_url_rule('/', view_func=categoryAPI.as_view('categoryview'), methods=['GET'])

# @bp.route('/', view_func=categoryAPI.as_view('categoryview'), methods=['GET', 'POST'])
# def index():
    # if request.method
    #return render_template('index.html')
    #return '<p>Hello world!</p>'