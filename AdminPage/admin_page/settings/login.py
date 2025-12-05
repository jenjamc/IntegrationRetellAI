from flask import Flask
from flask_login import LoginManager

from admin_page.models.admin_page import AdminUser
from admin_page.settings.db import db


def init_login_manager(app: Flask):
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id: str) -> 'AdminUser':
        return db.session.query(AdminUser).get(user_id)
