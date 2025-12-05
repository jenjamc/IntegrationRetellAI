from admin_page.app import create_app
from admin_page.settings.db import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
