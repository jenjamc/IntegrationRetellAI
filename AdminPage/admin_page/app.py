from flask import Flask
from flask_admin import Admin

from admin_page import settings
from admin_page import version
from admin_page.models.admin_page import AdminPermission
from admin_page.models.admin_page import AdminRole
from admin_page.models.admin_page import AdminUser
from admin_page.settings.db import db
from admin_page.settings.login import init_login_manager
from admin_page.views.admin_page.permission import AdminPermissionView
from admin_page.views.admin_page.roles import AdminRolesView
from admin_page.views.admin_page.users import AdminUsersView
from admin_page.views.base.admin import AdminIndexView


def init_views(admin_app: 'Admin') -> None:
    # Admin page
    admin_app.add_view(AdminUsersView(AdminUser, db.session, name='Admin Users', category='Admin Page'))
    admin_app.add_view(AdminRolesView(AdminRole, db.session, name='Roles', category='Admin Page'))
    admin_app.add_view(AdminPermissionView(AdminPermission, db.session, name='Permissions', category='Admin Page'))


def create_app() -> Flask:
    app = Flask(__name__)

    app.secret_key = settings.SECRET_KEY
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_POOL_TIMEOUT'] = None
    app.config['SQLALCHEMY_POOL_SIZE'] = None
    app.config['SQLALCHEMY_ECHO'] = settings.DEBUG
    app.config['DEBUG'] = settings.DEBUG
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.database_uri + settings.DB_NAME_ADMIN_PAGE
    app.config['SQLALCHEMY_BINDS'] = {
        'admin_page': settings.database_uri + settings.DB_NAME_ADMIN_PAGE,
        'user_manager': settings.database_uri + settings.DB_NAME_USER_MANAGER,
    }

    admin = Admin(
        app=app,
        name=f'Stobox4 Admin {version}',
        template_mode='bootstrap3',
        base_template='master.html',
        index_view=AdminIndexView(),
    )
    db.init_app(app)
    init_views(admin)
    init_login_manager(app)
    return app
