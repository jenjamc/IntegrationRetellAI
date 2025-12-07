from flask import flash

from admin_page.models.user_manager import Balance
from admin_page.settings.db import db
from admin_page.views.base.base_model import BaseModelView


class BalanceAdjustmentView(BaseModelView):

    def on_model_change(self, form, model, is_created):
        if is_created:
            balance = db.session.query(Balance).filter_by(tenant_id=model.tenant.id).first()
            if balance:
                balance.current_balance += model.delta_dollars
                db.session.add(balance)
                flash('Balance updated', 'success')
            else:
                flash('Balance not found', 'error')