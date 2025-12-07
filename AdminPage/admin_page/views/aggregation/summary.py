from flask_admin import BaseView
from flask_admin import expose
from sqlalchemy import func

from admin_page.models.user_manager import Balance
from admin_page.models.user_manager import Call
from admin_page.models.user_manager import Tenant
from admin_page.models.user_manager import User
from admin_page.settings.db import db


class ClientsSummaryView(BaseView):
    @expose('/')
    def index(self):
        clients = self.get_clients_summary()
        return self.render('admin/clients_summary.html', clients=clients)

    @staticmethod
    def get_clients_summary():
        query = (
            db.session.query(
                func.concat(User.first_name, ' ', User.last_name).label('name'),
                Tenant.agent_id,
                func.count(Call.id).label('total_calls'),
                func.coalesce(func.sum(Call.billed_seconds) / 60, 0).label('total_minutes'),
                func.coalesce(Balance.current_balance, 0).label('current_balance')
            )
            .join(User, User.tenant_id == Tenant.id)
            .outerjoin(Call, Call.tenant_id == Tenant.id)
            .outerjoin(Balance, Balance.tenant_id == Tenant.id)
            .group_by(Tenant.id, Balance.current_balance, User.first_name, User.last_name)
            .order_by(User.first_name, User.last_name)
        )

        return query.all()