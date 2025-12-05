from admin_page.views.base.base_model import BaseModelView


class AdminUsersView(BaseModelView):
    column_list = ('sub', 'role')
    column_editable_list = ('role',)
    form_columns = ('role',)
