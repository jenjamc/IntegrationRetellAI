from admin_page.views.base.base_model import BaseModelView


class UsersView(BaseModelView):
    form_columns = ('email', 'first_name', 'last_name', 'tenant', 'password_hash')
