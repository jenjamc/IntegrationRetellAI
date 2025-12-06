from flask_admin import BaseView
from flask_admin.contrib.sqla import ModelView
from sqlalchemy import ARRAY

from admin_page.views.base.permissions_view import PermissionsViewMixin


class BaseCustomView(PermissionsViewMixin, BaseView):
    pass


class BaseModelView(PermissionsViewMixin, ModelView):
    create_modal = False
    edit_modal = False
    can_export = True
    can_create = True
    can_edit = True
    can_delete = True
    can_set_page_size = True
    can_view_details = True
    named_filter_urls = True
    simple_list_pager = True
    column_default_sort = ('id', True)

    def __new__(cls, model, session, **kwargs):
        instance = super(BaseModelView, cls).__new__(cls)

        cols = []
        for col in model.__table__.columns:
            if not isinstance(col.type, ARRAY):
                cols.append(col.name)

        column_list = tuple(cols)

        if cls.column_filters is not None:
            column_list = column_list + cls.column_filters

        instance.column_filters = column_list
        instance.column_sortable_list = model.__table__.columns.keys()
        return instance
