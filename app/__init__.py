from flask import Flask
from config import Config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# init Login Manager
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = 'Please log in to add product to your cart'
login.login_message_category = 'warning'
#init database
db = SQLAlchemy()
#init Migrate
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    login.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from .blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from .blueprints.shop import bp as shop_bp
    app.register_blueprint(shop_bp)

    from .blueprints.cart import bp as cart_bp
    app.register_blueprint(cart_bp)

    return app