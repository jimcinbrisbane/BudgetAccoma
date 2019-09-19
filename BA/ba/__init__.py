from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

db=SQLAlchemy()


def create_app():
    app=Flask(__name__)
    app.debug=True
    app.secret_key='thisisasecretkey122'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///travel123.sqlite'
    #initialize db with flask app
    db.init_app(app)
    @app.errorhandler(404)
    def not_found(e):
       return render_template('404.html'),404

    boostrap = Bootstrap(app)

    from .views import mainbp
    app.register_blueprint(mainbp)

    return app




    

