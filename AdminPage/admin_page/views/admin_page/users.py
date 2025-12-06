from admin_page.views.base.base_model import BaseModelView


class AdminUsersView(BaseModelView):
    column_list = ('email', 'role')
    column_editable_list = ('role',)
