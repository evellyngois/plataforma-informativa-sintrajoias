from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from .config import Config
from .models import Base


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(Config)

    if test_config:
        app.config.update(test_config)

    engine = create_engine(app.config["DATABASE_URL"], future=True)
    session_factory = sessionmaker(bind=engine, autoflush=False, autocommit=False)
    db_session = scoped_session(session_factory)

    app.extensions["db_engine"] = engine
    app.extensions["db_session"] = db_session

    Base.metadata.create_all(engine)

    from .routes import bp
    app.register_blueprint(bp)

    @app.teardown_appcontext
    def remove_session(exception=None):
        db_session.remove()

    return app
