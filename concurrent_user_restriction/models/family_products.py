from odoo import api, fields, models
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError
from odoo.http import request


class FamilyProducts(models.Model):
    _inherit = 'family.products'

    def action_discontinue(self):
        if self.env.user.has_groups('pim_ext.group_family_product_user_write'):
            if self.family_id.editing:
                if not self.family_id.edit_session_name:
                    raise ValidationError("Another user is editing. Please reload and try again.")
                elif self.family_id.editing and self.family_id.edit_session_name != request.session.sid:
                    raise ValidationError("Another user is editing. Please reload and try again.")
        super().action_discontinue()

    def action_continue(self):
        if self.env.user.has_groups('pim_ext.group_family_product_user_write'):
            if self.family_id.editing:
                if not self.family_id.edit_session_name:
                    raise ValidationError("Another user is editing. Please reload and try again.")
                elif self.family_id.editing and self.family_id.edit_session_name != request.session.sid:
                    raise ValidationError("Another user is editing. Please reload and try again.")
        super().action_continue()