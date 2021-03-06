from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from berenice.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from berenice.users.routes import users
    from berenice.posts.routes import posts
    from berenice.main.routes import main
    from berenice.items.routes import items
    from berenice.dash_app.routes import dash_app
    from berenice.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(items)
    app.register_blueprint(dash_app)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app
