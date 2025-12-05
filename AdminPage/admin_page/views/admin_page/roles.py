from admin_page.views.base.base_model import BaseModelView


class AdminRolesView(BaseModelView):
    column_details_list = (
        'id',
        'created',
        'updated',
        'name',
        'permissions',
    )

    form_excluded_columns = (
        'created',
        'updated',
        'admins',
    )
