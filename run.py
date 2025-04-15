from app import create_app
from app.models import db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)
from app import create_app
from app.models import db, User
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app, db)

# Only run this when executing this file directly
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("✅ Tables created successfully.")

# from app import create_app

# # Create the app instance
# app = create_app()

# if __name__ == "__main__":
#     app.run(debug=True)
