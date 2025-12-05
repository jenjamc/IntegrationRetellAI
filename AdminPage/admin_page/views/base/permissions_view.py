from flask import flash
from flask import redirect
from flask import url_for
from flask_login import current_user
from wtforms import Form

from admin_page.models.admin_page.base import BaseModel
from admin_page.settings.db import db


class PermissionsViewMixin:
    def is_accessible(self):
        return not current_user.is_anonymous

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('admin.login_view'))

        if not self.is_visible():
            flash("Don't have permissions", category='error')
            return redirect(url_for('admin.index'))

    def is_visible(self) -> bool:
        if not current_user.role:
            return False

        admin_permissions = [permission.name for permission in current_user.role.permissions]
        if self.name in admin_permissions:
            self.update_permissions(admin_permissions)
            return True
        return False

    def update_permissions(self, admin_permissions) -> None:
        self.can_create = self.name + '_can_create' in admin_permissions
        self.can_delete = self.name + '_can_delete' in admin_permissions
        self.can_edit = self.name + '_can_edit' in admin_permissions
        self.can_view_details = self.name + '_can_view_details' in admin_permissions
