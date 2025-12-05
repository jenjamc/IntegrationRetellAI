from admin_page.views.base.base_model import BaseModelView


class AdminPermissionView(BaseModelView):
    can_create = False
    can_edit = False
    can_delete = False
