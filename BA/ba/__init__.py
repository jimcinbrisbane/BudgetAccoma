from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

#init database
db=SQLAlchemy()


def create_app():
    #init app   
    app=Flask(__name__)
    app.debug=True
    app.secret_key='thisisasecretkey122'
    #the folder to store images
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    #connectdb
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///travel123.sqlite'
    #initialize db with flask app
    db.init_app(app)
    # error handler
    @app.errorhandler(404)
    def not_found(e):
       return render_template('404.html'),404
   # get bootstrap init
    boostrap = Bootstrap(app)
    # blue print
    from .views import mainbp
    app.register_blueprint(mainbp)

    return app




    

