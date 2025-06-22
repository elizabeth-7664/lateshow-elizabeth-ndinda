from flask import Flask
from config import Config
from extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from routes.episodes import episodes_bp
    from routes.guests import guests_bp
    from routes.appearances import appearances_bp

    app.register_blueprint(episodes_bp)
    app.register_blueprint(guests_bp)
    app.register_blueprint(appearances_bp)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
