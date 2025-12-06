import flask_admin
import flask_login
from flask import redirect
from flask import request
from flask import url_for
from flask_admin import expose

from admin_page.forms.base.login import LoginAdminForm
from admin_page.models.admin_page import AdminUser
from admin_page.settings.db import db


class AdminIndexView(flask_admin.AdminIndexView):
    @expose('/')
    def index(self):
        if not flask_login.current_user.is_authenticated:
            return redirect(url_for('.login_view'))
        return self.render(self._template)

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        form = LoginAdminForm(request.form)
        if request.method == 'POST' and form.validate():
            user = self._get_admin_user(form.data['username'], form.data['password'])
            if user:
                flask_login.login_user(user)

        if flask_login.current_user.is_authenticated:
            return redirect(url_for('.index'))

        self._template_args['form'] = form
        return super(AdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        flask_login.logout_user()
        return redirect(url_for('.index'))

    @staticmethod
    def _get_admin_user(email: str, password: str) -> AdminUser | None:
        admin_user = db.session.query(AdminUser).filter_by(email=email, password=password).first()
        if not admin_user:
            return None

        return admin_user
